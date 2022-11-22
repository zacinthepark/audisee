import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";
import createPersistedState from "vuex-persistedstate";

Vue.use(Vuex);

const API_URL = "http://127.0.0.1:8000";

export default new Vuex.Store({
  plugins: [createPersistedState()],
  state: {
    movies: [],
    musics: [],
    myMovies: [],
    myTracks: [],
    token: null,
  },
  getters: {
    myMovieCount(state) {
      return state.myMovies.length;
    },
    myTrackCount(state) {
      return state.myTracks.length;
    },
  },
  mutations: {
    GET_MOVIES(state, movies) {
      state.movies = movies;
    },
    GET_MUSICS(state, musics) {
      state.musics = musics;
    },
    GET_MY_MOVIES(state, myMovies) {
      state.myMovies = myMovies;
    },
    GET_MY_TRACKS(state, myTracks) {
      state.myTracks = myTracks;
    },
    SAVE_TOKEN(state, token) {
      state.token = token;
    },
  },
  actions: {
    getMovies(context) {
      axios({
        method: "get",
        url: `${API_URL}/api/v1/movies/`,
      })
        .then((response) => {
          context.commit("GET_MOVIES", response.data);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    getMusics(context) {
      axios({
        method: "get",
        url: `${API_URL}/api/v1/musics`,
      })
        .then((response) => {
          console.log(response.data);
          context.commit("GET_MUSICS", response.data);
        })
        .catch((error) => {
          console.log(error);
        });
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
          context.commit("GET_MY_MOVIES", response.data);
        })
        .catch((error) => {
          console.log(error);
        });
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
          context.commit("GET_MY_TRACKS", response.data);
        })
        .catch((error) => {
          console.log(error);
        });
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
          context.commit("SAVE_TOKEN", response.data.key);
        })
        .catch((error) => {
          console.log(error);
        });
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
          context.commit("SAVE_TOKEN", response.data.key);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  modules: {},
});
