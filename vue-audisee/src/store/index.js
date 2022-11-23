import Vue from "vue"
import Vuex from "vuex"
import axios from "axios"
import createPersistedState from "vuex-persistedstate"

Vue.use(Vuex)

const API_URL = "http://127.0.0.1:8000"

export default new Vuex.Store({
  plugins: [createPersistedState()],
  state: {
    movies: [],
    recommendedMovies: [],
    recommendedMood: "",
    musics: [],
    myMovies: [],
    myTracks: [],
    token: null,
  },
  getters: {
    myMovieCount(state) {
      return state.myMovies.length
    },
    myTrackCount(state) {
      return state.myTracks.length
    },
  },
  mutations: {
    GET_MOVIES(state, movies) {
      state.movies = movies
    },
    GET_MUSICS(state, musics) {
      state.musics = musics
    },
    GET_MY_MOVIES(state, myMovies) {
      state.myMovies = myMovies
    },
    GET_MY_TRACKS(state, myTracks) {
      state.myTracks = myTracks
    },
    DELETE_MY_MOVIE(state, myMovies) {
      state.myMovies = myMovies
    },
    DELETE_MY_TRACK(state, myTracks) {
      state.myTracks = myTracks
    },
    GET_MOVIE_RECOMMEND_ONE(state, movies) {
      state.recommendedMovies = movies
    },
    GET_MOVIE_RECOMMEND_TWO(state, movies) {
      state.recommendedMovies = movies
    },
    GET_MOVIE_RECOMMEND_THREE(state, movies) {
      state.recommendedMovies = movies
    },
    GET_MOVIE_RECOMMEND_FOUR(state, movies) {
      state.recommendedMovies = movies
    },
    GET_MOVIE_RECOMMEND_FIVE(state, movies) {
      state.recommendedMovies = movies
    },
    GET_MOVIE_RECOMMEND_SIX(state, movies) {
      state.recommendedMovies = movies
    },
    GET_MOVIE_RECOMMEND_SEVEN(state, movies) {
      state.recommendedMovies = movies
    },
    GET_MOVIE_RECOMMEND_EIGHT(state, movies) {
      state.recommendedMovies = movies
    },
    GET_MOVIE_RECOMMEND_NINE(state, movies) {
      state.recommendedMovies = movies
    },
    GET_MOVIE_RECOMMEND_TEN(state, movies) {
      state.recommendedMovies = movies
    },
    SAVE_TOKEN(state, token) {
      state.token = token
    },
  },
  actions: {
    getMovies(context) {
      axios({
        method: "get",
        url: `${API_URL}/api/v1/movies/`,
      })
        .then((response) => {
          context.commit("GET_MOVIES", response.data)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    getMusics(context) {
      axios({
        method: "get",
        url: `${API_URL}/api/v1/musics`,
      })
        .then((response) => {
          console.log(response.data)
          context.commit("GET_MUSICS", response.data)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    getMyMovies(context) {
      axios({
        method: "get",
        url: `${API_URL}/playlist/movies/`,
        headers: {
          Authorization: `Token ${this.state.token}`,
        },
      })
        .then((response) => {
          context.commit("GET_MY_MOVIES", response.data)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    getMyTracks(context) {
      axios({
        method: "get",
        url: `${API_URL}/playlist/tracks/`,
        headers: {
          Authorization: `Token ${this.state.token}`,
        },
      })
        .then((response) => {
          context.commit("GET_MY_TRACKS", response.data)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    deleteMyMovie(context, movie_id) {
      axios({
        method: "delete",
        url: `${API_URL}/playlist/movies/${movie_id}`,
        headers: {
          Authorization: `Token ${this.state.token}`,
        },
      })
        .then((response) => {
          context.commit("DELETE_MY_MOVIE", response.data)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    deleteMyTrack(context, track_id) {
      axios({
        method: "delete",
        url: `${API_URL}/playlist/tracks/${track_id}`,
        headers: {
          Authorization: `Token ${this.state.token}`,
        },
      })
        .then((response) => {
          context.commit("DELETE_MY_TRACK", response.data)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    getMovieRecommendOne(context, mood) {
      this.recommendedMood = mood
      console.log(mood)
      console.log(this.recommendedMood)
      axios({
        method: "get",
        url: `${API_URL}/api/v1/movies/${mood}/`,
        headers: {
          Authorization: `Token ${this.state.token}`,
        },
      })
        .then((response) => {
          console.log(response.data)
          context.commit("GET_MOVIE_RECOMMEND_ONE", response.data)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    getMovieRecommendTwo(context, mood) {
      this.recommendedMood = mood
      console.log(this.recommendedMood)
      axios({
        method: "get",
        url: `${API_URL}/api/v1/movies/${mood}/`,
        headers: {
          Authorization: `Token ${this.state.token}`,
        },
      })
        .then((response) => {
          // console.log(response.data)
          context.commit("GET_MOVIE_RECOMMEND_TWO", response.data)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    getMovieRecommendThree(context, mood) {
      this.recommendedMood = mood
      axios({
        method: "get",
        url: `${API_URL}/api/v1/movies/${mood}/`,
        headers: {
          Authorization: `Token ${this.state.token}`,
        },
      })
        .then((response) => {
          // console.log(response.data)
          context.commit("GET_MOVIE_RECOMMEND_THREE", response.data)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    getMovieRecommendFour(context, mood) {
      this.recommendedMood = mood
      axios({
        method: "get",
        url: `${API_URL}/api/v1/movies/${mood}/`,
        headers: {
          Authorization: `Token ${this.state.token}`,
        },
      })
        .then((response) => {
          // console.log(response.data)
          context.commit("GET_MOVIE_RECOMMEND_FOUR", response.data)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    getMovieRecommendFive(context, mood) {
      this.recommendedMood = mood
      axios({
        method: "get",
        url: `${API_URL}/api/v1/movies/${mood}/`,
        headers: {
          Authorization: `Token ${this.state.token}`,
        },
      })
        .then((response) => {
          // console.log(response.data)
          context.commit("GET_MOVIE_RECOMMEND_FIVE", response.data)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    getMovieRecommendSix(context, mood) {
      this.recommendedMood = mood
      axios({
        method: "get",
        url: `${API_URL}/api/v1/movies/${mood}/`,
        headers: {
          Authorization: `Token ${this.state.token}`,
        },
      })
        .then((response) => {
          // console.log(response.data)
          context.commit("GET_MOVIE_RECOMMEND_SIX", response.data)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    getMovieRecommendSeven(context, mood) {
      this.recommendedMood = mood
      axios({
        method: "get",
        url: `${API_URL}/api/v1/movies/${mood}/`,
        headers: {
          Authorization: `Token ${this.state.token}`,
        },
      })
        .then((response) => {
          // console.log(response.data)
          context.commit("GET_MOVIE_RECOMMEND_SEVEN", response.data)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    getMovieRecommendEight(context, mood) {
      this.recommendedMood = mood
      axios({
        method: "get",
        url: `${API_URL}/api/v1/movies/${mood}/`,
        headers: {
          Authorization: `Token ${this.state.token}`,
        },
      })
        .then((response) => {
          // console.log(response.data)
          context.commit("GET_MOVIE_RECOMMEND_EIGHT", response.data)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    getMovieRecommendNine(context, mood) {
      this.recommendedMood = mood
      axios({
        method: "get",
        url: `${API_URL}/api/v1/movies/${mood}/`,
        headers: {
          Authorization: `Token ${this.state.token}`,
        },
      })
        .then((response) => {
          // console.log(response.data)
          context.commit("GET_MOVIE_RECOMMEND_NINE", response.data)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    getMovieRecommendTen(context, mood) {
      this.recommendedMood = mood
      axios({
        method: "get",
        url: `${API_URL}/api/v1/movies/${mood}/`,
        headers: {
          Authorization: `Token ${this.state.token}`,
        },
      })
        .then((response) => {
          // console.log(response.data)
          context.commit("GET_MOVIE_RECOMMEND_TEN", response.data)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    signUp(context, payload) {
      axios({
        method: "post",
        url: `${API_URL}/accounts/signup/`,
        data: {
          username: payload.username,
          password1: payload.password1,
          password2: payload.password2,
          first_name: payload.firstName,
          last_name: payload.lastName,
        },
      })
        .then((response) => {
          context.commit("SAVE_TOKEN", response.data.key)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    logIn(context, payload) {
      axios({
        method: "post",
        url: `${API_URL}/accounts/login/`,
        data: {
          username: payload.username,
          password: payload.password,
        },
      })
        .then((response) => {
          context.commit("SAVE_TOKEN", response.data.key)
        })
        .catch((error) => {
          console.log(error)
        })
    },
  },
  modules: {},
})
