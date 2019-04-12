import { API } from '@/js/api/api'

export const userModule = {

  namespaced: true,

  state: {
    cartItems: null,
    cart: null,
    userId: '1',
    avatar: ''
  },

  getters: {
    cartContains: (state) => (ingredientId) => {
      return !!state.cartItems.find(item => item.id_Ingredient === ingredientId)
    },
    avatar: (state) => (user) => {
      if (user) {
        return user.avatar || `${process.env.BASE_URL}images/default-avatar.png`
      }
      return state.avatar || `${process.env.BASE_URL}images/default-avatar.png`
    }
  },

  mutations: {
    clear (state) {
      state.userId = null
      state.cart = null
      state.cartItems = null
      state.avatar = null
    },
    setCartItems (state, cartItems) {
      if (cartItems) state.cartItems = cartItems
    },
    setCart (state, cart) {
      if (cart) state.cart = cart
    }
  },

  actions: {
    async loadCart (context) {
      const cart = await API.getUserCart(context.state.userId)
      if (!cart.error) {
        context.commit('setCart', cart)
      }
      if (context.state.cart) {
        const cartItems = await API.getCartItems(context.state.cart.id)
        if (!cartItems.error) {
          context.commit('setCartItems', cartItems)
        }
      }
    },
    async addCartItem (context, ingredientId) {
      if (context.state.cart) {
        await API.addCartItem(context.state.cart.id, ingredientId)
        context.dispatch('loadCart')
      }
    },
    async removeCartItem (context, ingredientId) {
      if (context.state.cart) {
        await API.removeCartItem(context.state.cart.id, ingredientId)
        context.dispatch('loadCart')
      }
    }
  }

}
