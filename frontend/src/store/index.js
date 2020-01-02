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
    userTweetList: [],
    followersTweetList: [],
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
    SETUSERTWEETS: (state, userTweetList) => {
      state.userTweetList = userTweetList;
    },
    SETFOLLOWERTWEETS: (state, followerTweets) => {
      state.followersTweetList = followerTweets;
    },
    CHANGEACTIVETAB: (state, newActiveTab) => {
      state.activeTab = newActiveTab;
    },
    LOGOUT: state => {
      state.authToken = "";
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
      axios.defaults.headers = {
        "Content-Type": "application/json"
      };
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
    createNewUser: ({ dispatch }, payload) => {
      axios
        .post("http://127.0.0.1:8000/auth/users/", {
          first_name: payload.firstName,
          last_name: payload.lastName,
          username: payload.username,
          password: payload.password,
          re_password: payload.password,
          email: payload.email
        })
        .then(response => {
          dispatch("logIn", payload);
          return response.data;
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
          // dispatch("getFollowers");
          localStorage.setItem(
            "auth_token",
            JSON.stringify(data["auth_token"])
          );
          dispatch("getUserTweets");
        })
        .catch(error => {
          console.log(error);
        });
    },
    getUserTweets: ({ state, commit }) => {
      axios
        .get(`http://127.0.0.1:8000/api/tweets/list/${state.user.id}`)
        .then(response => {
          commit("SETUSERTWEETS", response.data);
        })
        .catch(error => {
          return error;
        });
    },
    getFollowers: ({ state, dispatch }) => {
      var follower_ids = [];
      axios
        .get(`http://127.0.0.1:8000/api/tweets/followers/${state.user.id}`)
        .then(response => {
          follower_ids = response.data.map(obj => {
            return obj.followed_id;
          });
          dispatch("getFollowerTweets", follower_ids);
        })
        .catch(error => {
          return error;
        });
    },
    getFollowerTweets: ({ commit }, follower_ids) => {
      axios
        .get("http://127.0.0.1:8000/api/tweets/alldata/", {
          params: follower_ids
        })
        .then(response => {
          var followerTweets = [];
          for (var x = 0; x < response.data.length; x++) {
            var obj = {};
            obj["author"] = response.data[x][0];
            obj["first_name"] = response.data[x][1];
            obj["last_name"] = response.data[x][2];
            obj["tweet_text"] = response.data[x][3];
            obj["created_on"] = response.data[x][4];
            followerTweets.push(obj);
          }
          commit("SETFOLLOWERTWEETS", followerTweets);
        })
        .catch(error => {
          return error;
        });
    },
    logout: context => {
      axios
        .post("http://127.0.0.1:8000/auth/token/logout/", {
          Authorization: "Token " + context.authToken
        })
        .then(response => {
          context.commit("LOGOUT");
          router.push({ path: "/" });
          return response;
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
