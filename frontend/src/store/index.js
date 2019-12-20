/* eslint-disable no-console */
import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";
import router from "../router/index.js";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    user: {},
    authToken: "",
    info: "",
    error: {},
    tweetList: {},
    activeTab: ""
  },
  getters: {
    user: state => {
      return state.user;
    }
  },
  mutations: {
    SETUSERINFO: (state, userInfo) => {
      state.user = userInfo;
    },
    SETAUTHTOKEN: (state, token) => {
      state.authToken = token;
    },
    SETTWEETS: (state, tweetList) => {
      state.tweetList = tweetList;
    },
    CHANGEACTIVETAB: (state, newActiveTab) => {
      state.activeTab = newActiveTab;
    }
  },
  actions: {
    initializeToken: ({ dispatch }) => {
      if (localStorage.auth_token) {
        let data = {
          auth_token: JSON.parse(localStorage.getItem("auth_token"))
        };
        dispatch("getUserInfo", data);
      }
    },
    logIn: ({ dispatch }, data) => {
      axios
        .post("http://127.0.0.1:8000/auth/token/login/", {
          email: data.email,
          password: data.password
        })
        .then(response => {
          dispatch("getUserInfo", response.data);
          dispatch("changeActiveTab", "profile");
          router.push({ path: "/myprofile" });
        })
        .catch(error => {
          console.log(error);
        });
    },
    getUserInfo: ({ commit, dispatch }, data) => {
      axios.defaults.headers = {
        Authorization: "Token " + data["auth_token"]
      };
      axios
        .get("http://127.0.0.1:8000/auth/users/me/")
        .then(response => {
          commit("SETUSERINFO", response.data);
          commit("SETAUTHTOKEN", data["auth_token"]);
          dispatch("getTweets");
          localStorage.setItem(
            "auth_token",
            JSON.stringify(data["auth_token"])
          );
        })
        .catch(error => {
          console.log(error);
        });
    },
    getTweets: ({ commit }) => {
      axios
        .get("http://127.0.0.1:8000/api/tweets/alldata/")
        .then(response => {
          commit("SETTWEETS", response.data);
        })
        .catch(error => {
          return error;
        });
    },
    changeActiveTab: ({ commit }, newActiveTab) => {
      commit("CHANGEACTIVETAB", newActiveTab);
    }
  },
  modules: {}
});
