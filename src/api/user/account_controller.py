from dataclasses import asdict
from flask import Blueprint
from flask.app import Flask
from flask_jwt import jwt_required, current_identity
from src.api import response
from src.api.requests import parse_body
from src.api.user.user_responses import AccountResponse, AddressResponse
from src.api.user.user_edition_request import AccountEditionRequest, AddressEditionRequest
from src.application.account.user_edition_dto import AccountInfoEditionDto, AddressInfoEditionDto
from src.context import user_finding_usecase, user_editing_usecase


routes = Blueprint('account', __name__, url_prefix='/user/account')


@routes.route('', methods=['GET'])
@jwt_required()
@response.handleExceptions
def get_current_user_account():
    account = user_finding_usecase.find_account_of(current_identity.id)
    address = user_finding_usecase.find_adress_for_account(account.id)
    response_data = AccountResponse(
        id=account.id,
        id_User=account.id_User,
        id_Address=account.id_Address,
        firstName=account.firstName,
        lastName=account.lastName,
        email=account.email,
        address=AddressResponse(**asdict(address))
    )
    return response.success(response_data)


@routes.route('', methods=['PATCH'])
@jwt_required()
@response.handleExceptions
@parse_body(AccountEditionRequest)
def modify_current_user_account(request_body: AccountEditionRequest):
    try:
        account_edition_dto = AccountInfoEditionDto(
            email=request_body.email,
            password=request_body.password
        )
        account = user_editing_usecase.update_account(current_identity.id, account_edition_dto)
        address = user_finding_usecase.find_adress_for_account(account.id)
        response_data = AccountResponse(
            id=account.id,
            id_User=account.id_User,
            id_Address=account.id_Address,
            firstName=account.firstName,
            lastName=account.lastName,
            email=account.email,
            address=AddressResponse(**asdict(address))
        )
        return response.success(response_data)
    except Exception as e:
        return response.error(e)


@routes.route('/address', methods=['GET'])
@jwt_required()
@response.handleExceptions
def get_current_user_address():
    account = user_finding_usecase.find_account_of(current_identity.id)
    address = user_finding_usecase.find_adress_for_account(account.id)
    return response.success(address)


@routes.route('/address', methods=['PATCH'])
@jwt_required()
@response.handleExceptions
@parse_body(AddressEditionRequest)
def modify_current_user_address(request_body: AddressEditionRequest):
    try:
        address_edition_dto = AddressInfoEditionDto(
            country=request_body.country,
            city=request_body.city,
            street=request_body.street,
            apartment=request_body.apartment,
            number=request_body.number
        )
        address = user_editing_usecase.update_address(current_identity.id, address_edition_dto)
        return response.success(address)
    except Exception as e:
        return response.error(e)


def register_routes(flask_app: Flask):
    flask_app.register_blueprint(routes)
