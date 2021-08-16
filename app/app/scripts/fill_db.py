from dotenv import load_dotenv
load_dotenv()

import random
from datetime import datetime
from app.infra.db.daos.recipe import RecipeCommentDao, RecipeRatingDao, LikeRecipeDao
from app.infra.db.models.recipe import LikeRecipeModel, CommentModel, RatingModel
from app.infra.db.daos.ingredient import IngredientDao, QuantityUnitDao
from app.infra.db.models.ingredient import IngredientModel
from app.infra.db.daos.cart import CartDao, CartItemDao, CommandDao
from app.infra.db.models.cart import CartModel, CartItemModel, CommandModel
from app.application.account.signup_dto import AccountInfo, SignupDto, UserInfo, AddressInfo
from app.application.recipe.recipe_creation_dto import RecipeCreationInfo, RecipeIngredientCreationInfo, RecipeCreationDto

ingredientDao = IngredientDao()
cartItemDao = CartItemDao()
quantityUnitDao = QuantityUnitDao()
ratingDao = RecipeRatingDao()
commentDao = RecipeCommentDao()
likeRecipeDao = LikeRecipeDao()
commandDao = CommandDao()
cartDao = CartDao()

from app.context import signup_usecase, recipe_creation_usecase, db_connection_2

lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi pulvinar pharetra bibendum. Ut eget risus nec risus finibus hendrerit in non tortor. Pellentesque maximus ligula et turpis faucibus cursus. Donec vel nunc metus. Quisque sagittis mattis dui vel varius. Aliquam iaculis interdum lacinia. Nam euismod lectus id maximus sodales. Nam id magna dictum, semper nisl vel, ornare ligula. Sed condimentum metus quis leo pharetra, quis semper urna aliquam. Fusce consectetur accumsan augue sit amet iaculis. Suspendisse volutpat urna vitae fermentum eleifend. Maecenas sapien leo, gravida vitae pellentesque quis, efficitur in erat. Maecenas elementum euismod hendrerit. Mauris sagittis massa a orci."
words = ["Hogym", "Celloggimbur", "Laglesgim", "Sylcyllis", "Morbir", "Limgem", "Silgimculnir", "Narmar", "Solgamberthi", "Cyllig", "Thalomorn", "Rluggum", "Ornbar", "Merhosyl", "Callisthunir", "Thaligber", "Limbarmar", "Lishalllumcal", "Berthe", "Hathulemhe", "Colmorhi", "Salthalegorn", "Birmircyl", "Bermor", "Morlag", "Barbirorn", "Burmir", "Humarhamur", "Leglam", "Hugimirn", "Berburthamur", "Lasloglum", "Gomlamthi", "Narmarborern", "Lomlos", "Urnlasho", "Hical", "Hisol", "Leshe", "Gumsalculsil", "Morcalsul", "Barlugha", "Salhu", "Celmorgember", "Byrhebyr", "Birhogim", "Helisloshi", "Syllas", "Gymcalhober", "Gimcullegirn", "Borlessil", "Thitha", "Cylcelnor", "Borbyrhulys", "Loglistha", "Silbartha", "Orncilbirgom", "Lasnormer", "Lumsolthalig", "Burlyscul", "Murgomhellhi", "Thatheluslag", "Lyshallluslam", "Mirborcil", "Nircalbur", "Barlugarn", "Gimcul", "Thulam", "Hecolha", "Ornmur", "Lamber", "Sulleshe", "Lomlember", "Loscal", "Calornthilog", "Limlesgam", "Thigomcul", "Laglyslomlis", "Erngomlig", "Gamlusmorcol", "Syllag", "Hothoirnlug", "Hesolmar", "Lugcul", "Thicolthu", "Narlescul", "Nirmersolurn", "Logcel", "Lasloglag", "Lessellamyrn", "Gymlys", "Thasal", "Silurnsellag", "Hallloslysbur", "Ligbir", "Burcylcel", "Narlisho" ,"Hosal","Liscal", "Sulbarmornar", "Tyfoxe", "Xusini", "Kidoxa", "Piphafy", "Chirra", "Rrobysu", "Jasu", "Quacy", "Laqui", "Nophe", "Mmyjyhe", "Quelli", "Jazo", "Mmichera", "Rroky", "Mmelli", "Girre", "Kibi", "Zafu", "Nowomi", "Dunummo", "Phasone", "Gipho", "Kyjado", "Senoze", "Gocahy", "Mmoha", "Mata", "Vupo", "Lochu", "Zeto", "Cycaci", "Llollace", "Cuphiwa", "Thexe", "Billu", "Matuko", "Rruxigu", "Bogu", "Vesi", "Wetu", "Jegi", "Gake", "Chullene", "Rruno", "Hyza", "Poru", "Nyxichi", "Fadylu", "Lajyse", "Phuxu", "Thehyko", "Quovavu", "Lleji", "Kynugy", "Mmyte", "Pakufa", "Sychecha", "Thine", "Sidemi", "Mmeka", "Jyfybo", "Mmuquoby", "Vuci", "Raci", "Zyhi", "Sujytho", "Cukemo", "Mixevo", "Thyxuwu", "Muphaba", "Pehide", "Thaserra", "Byjuwi", "Geka", "Zurruca", "Hymmy", "Thuju", "Rydu", "Jeduty", "Lluzali", "Rroce", "Sala", "Sipehu", "Pazasi", "Hagyga", "Nophy", "Rrammyca", "Kevygu", "Hellu", "Jimiru", "Llommiga", "Fasopy", "Navede", "Wireju", "Kotherru", "Cuphu", "Lloto", "Lledagy", "Syqua", "Zajerry", "Wipugo", "Sixare", "Gyka", "Bibowo", "Poje", "Mechiwi", "Juzuke", "Nyjige", "Zycu", "Govopy", "Nibo", "Tysy", "Viri", "Mmoxuby", "Boxemmi", "Xathe", "Mmocho", "Rycho", "Pijoly", "Mexo", "Thytha", "Gequo", "Rycypy", "Boquirri", "Zapu", "Gichu", "Rethu", "Gully", "Quoquafa", "Vozella", "Fibonu", "Dodyra", "Theky", "Sozawy", "Cehypy", "Rrotyhu", "Mowe", "Chusuny", "Pyru", "Dypu", "Juhuta", "Polo", "Phikotho", "Polymmo", "Hyse", "Suquajo", "Lletyjo", "Phata", "Fille", "Medy", "Cephellu", "Wogaha", "Quarrythy", "Mmanure", "Tumu", "Rothe", "Hapha", "Loxocho", "Coquawi", "Bonephe", "Suchu", "Mmiweso", "Mallyzy", "Wimma", "Rriwufi", "Nopho", "Pima", "Gyki"]
addr = ["St", "Ave", "Blvd", "Rd"]


def user_ids():
    with db_connection_2.transaction() as executor:
        return [user['id'] for user in executor.find_all('User')]

def cart_ids():
    with db_connection_2.transaction() as executor:
        return [cart['id'] for cart in executor.find_all('Cart')]

def ingredient_ids():
    with db_connection_2.transaction() as executor:
        return [ingredient['id'] for ingredient in executor.find_all('Ingredient')]

def recipe_ids():
    with db_connection_2.transaction() as executor:
        return [recipe['id'] for recipe in executor.find_all('Recipe')]


def clear_database():
    with db_connection_2.transaction() as executor:
        executor.execute("DELETE FROM RecipeIngredient;")
        executor.execute("DELETE FROM CartItem;")
        executor.execute("DELETE FROM LikeRecipe;")
        executor.execute("DELETE FROM Account;")
        executor.execute("DELETE FROM Command;")
        executor.execute("DELETE FROM Comment;")
        executor.execute("DELETE FROM Rating;")

        executor.execute("DELETE FROM Ingredient;")
        executor.execute("DELETE FROM Address;")
        executor.execute("DELETE FROM Recipe;")
        executor.execute("DELETE FROM Cart;")

        executor.execute("DELETE FROM User;")


def create_accounts(n: int, test_account: bool = True):
    if test_account:
        create_account(username="test", password="test")

    usernames = random.sample(words, n)
    for username in usernames:
        create_account(username=username)

def create_account(username: str, password: str = None):
    if not password:
        password = random.choice(words)

    firstName = random.choice(words)
    lastName = random.choice(words)

    signup_usecase.register_new_user(SignupDto(
        user=UserInfo(
            username=username
        ),
        account=AccountInfo(
            firstName=firstName,
            lastName=lastName,
            email=f"{firstName}.{lastName}@gmail.com",
            password=password
        ),
        address=AddressInfo(
            number=random.randint(1, 10000),
            street=f"{random.choice(words)} {random.choice(addr)}",
            city=random.choice(words),
            country=random.choice(words),
            apartment=random.randint(1, 100) if random.randint(0, 1) == 0 else None
        )
    ))

def create_ingredients(n: int):
    ingredient_names = random.sample(words, n)
    for ingredient_name in ingredient_names:
        ingredientModel = IngredientModel(
            id_IngredientType=random.randint(1, 13),
            id_QuantityUnit=random.randint(1, 13),
            name=ingredient_name,
            baseCost=round(random.random() * 15, 2),
            baseQuantity=random.randint(1, 12)
        )
        ingredientDao.save(ingredientModel)

def generateCartItems(max_per_cart: int):
    for cart_id in cart_ids():
        n_ingredients = random.randint(1, max_per_cart)
        ingredients_to_add = random.sample(ingredient_ids(), n_ingredients)
        for ingredient_id in ingredients_to_add:
            cartItemModel = CartItemModel(
                id_Ingredient=ingredient_id,
                id_Cart=cart_id
            )
            cartItemDao.save(cartItemModel)

def create_recipes(n: int):
    all_ingredient_ids = ingredient_ids()
    all_user_ids = user_ids()

    for _ in range(n):
        n_ingredients = random.randint(3, 20)
        recipe_ingredient_ids = random.sample(all_ingredient_ids, n_ingredients)
        ingredients = []

        for ingredient_id in recipe_ingredient_ids:
            quantities = quantityUnitDao.getAllQuantityUnitsByIngredientId(ingredient_id)
            quantity_ids = [q.id for q in quantities]

            ingredient = RecipeIngredientCreationInfo(
                id_Ingredient=ingredient_id,
                id_QuantityUnit=random.choice(quantity_ids),
                totalQuantity=random.randint(1, 999)
            )
            ingredients.append(ingredient)

        recipe_creation_usecase.create_recipe(RecipeCreationDto(
            recipe=RecipeCreationInfo(
                id_User=random.choice(all_user_ids),
                name=" ".join(random.sample(words, 3)),
                directives=lorem,
                description=lorem
            ),
            ingredients=ingredients
        ))

def generateRatings(max_per_user: int):
    for user_id in user_ids():
        recipes_to_rate = random.sample(recipe_ids(), random.randint(0, max_per_user))
        for recipe_id in recipes_to_rate:
            ratingModel = RatingModel(
                id_Recipe=recipe_id,
                id_User=user_id,
                value=random.randint(1, 5)
            )
            ratingDao.save(ratingModel)

def generateComments(n: int):
    for _ in range(n):
        commentModel = CommentModel(
            id_Recipe=random.choice(recipe_ids()),
            id_User=random.choice(user_ids()),
            text=lorem
        )
        commentDao.save(commentModel)

def generateLikes(max_per_user: int):
    for user_id in user_ids():
        recipes_to_like = random.sample(recipe_ids(), random.randint(0, max_per_user))
        for recipe_id in recipes_to_like:
            likeRecipeModel = LikeRecipeModel(
                id_Recipe=recipe_id,
                id_User=user_id
            )
            likeRecipeDao.save(likeRecipeModel)

def generateCommands(n: int):
    for _ in range(n):
        cartModel = CartModel(id_User=random.choice(user_ids()))
        cart = cartDao.save(cartModel)

        current_time = datetime.now()
        commandModel = CommandModel(
            id_Cart=cart.id,
            creationDate=current_time,
            arrivalDate=current_time
        )
        commandDao.save(commandModel)


if __name__ == "__main__":
    steps = [
        {'title': 'clearing database', 'action': clear_database},
        {'title': 'creating accounts', 'action': lambda: create_accounts(10)},
        {'title': 'creating ingredients', 'action': lambda: create_ingredients(30)},
        {'title': 'creating cart items', 'action': lambda: generateCartItems(5)},
        {'title': 'creating recipes', 'action': lambda: create_recipes(50)},
        {'title': 'creating recipe ratings', 'action': lambda: generateRatings(5)},
        {'title': 'creating recipe likes', 'action': lambda: generateLikes(3)},
        {'title': 'creating recipe comments', 'action': lambda: generateComments(100)},
        {'title': 'creating commands', 'action': lambda: generateCommands(30)},
    ]

    for i, step in enumerate(steps):
        print(f" - {i+1}/{len(steps)} {step['title']}...")
        step['action']()
