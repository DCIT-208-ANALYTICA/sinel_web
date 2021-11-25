import axios from "axios";

import { REGISTER_USER, REGISTER_USER_SUCCESSFUL, REGISTER_USER_FAILED } from './actionTypes';

const initialState = {
    access: localStorage.getItem('access'),
    refresh: localStorage.getItem('refresh'),
    isAuthenticated: null,
    user: null
}

const account = (state = initialState, action) => {
    const { type, payload } = action;
    switch (type) {
        case REGISTER_USER:
            return {
                ...state,
                user: null,
                loading: true,
                registrationError: null
            }
            break;
       
        case REGISTER_USER_SUCCESSFUL:
            return {
                ...state,
                isAuthenticated: true,
                loading: false,
            }
            break;
        case REGISTER_USER_FAILED: {
            return {
                ...state,
                user: null,
                loading: false,
                registrationError: payload
            }
        }
          
    }
    return state;
}

export default account;



export const register = (data) => {
    return (dispatch) => {
        axios.post("http://127.0.0.1:8000/api/v1/administrators/register/" , data)
        .then((res)=>{
            console.log("success");
            if (res.status === 200) {
                // localStorage.setItem("register", true);
                dispatch({
                    type: REGISTER_USER_SUCCESSFUL,
                })
                // history.push("/login");
            }
            })
            .catch((err) => {
            console.log(err);
        })
    }
}