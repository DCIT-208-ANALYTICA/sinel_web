import axios from "axios";

class APIClient {
    instance;
    constructor() {
        this.instance = axios.create({
            baseURL: "http://167.71.80.214/"
        })
    }

    async login({ email, password }) {
        const res = await this.instance.request({
            url: "api/v1/administrators/login/",
            headers: { 'Content-Type': 'application/json' },
            method: "post",
            data: {
                email_address: email,
                password: password
            }
        });

        return res;
    }
}

export default APIClient;