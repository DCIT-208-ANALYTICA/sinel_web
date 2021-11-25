import { REGISTER_USER, REGISTER_USER_SUCCESSFUL, REGISTER_USER_FAILED } from './actionTypes';
import axios from 'axios'


export const register = (email, username, password,) => async dispatch => {
    const config = {
        headers: {
            'Content-Type': 'application/json'
        }
    };

    const body = JSON.stringify({   email, password, username });

    try {
        const res = await axios.post(`ROUTE`, body, config);

        dispatch({
            type: REGISTER_USER_SUCCESSFUL,
            payload: res.data
        });
    } catch (err) {
        dispatch({
            type: REGISTER_USER_FAILED
        })
    }
};


export const registerUserSuccessful = (user) => {
    return {
        type: REGISTER_USER_SUCCESSFUL,
        payload: user
    }
}

export const registerUserFailed = (error) => {
    return {
        type: REGISTER_USER_FAILED,
        payload: error
    }
}