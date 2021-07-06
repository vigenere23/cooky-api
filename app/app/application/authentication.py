import bcrypt
from app.domain.exceptions import ForbiddenException
from app.infra.db.daos.user import UserDao, AccountDao


def ensure_same_user(resource_owner_id, current_user_id):
    if current_user_id != resource_owner_id:
        raise ForbiddenException()


def ensureIdentity(user_id, identity):
    if user_id != identity.id:
        raise ForbiddenException()


def authenticate(username, password):
    userDao = UserDao()
    accountDao = AccountDao()
    try:
        user = userDao.getByUsername(username)
        account = accountDao.getAccountByUserId(user.id)

        hashed_password = account.password
        if isinstance(hashed_password, bytearray):
            hashed_password = bytes(hashed_password)
        if not isinstance(hashed_password, bytes):
            hashed_password = hashed_password.encode()

        if bcrypt.checkpw(password.encode(), hashed_password):
            return user
    except Exception as e:
        print(e)
        return None


def get_identity(payload):
    userDao = UserDao()
    user_id = payload['identity']
    try:
        return userDao.getById(user_id)
    except Exception:
        return None