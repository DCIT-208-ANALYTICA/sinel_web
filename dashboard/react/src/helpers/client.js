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

    // contacts
    async getContact() {
        const token = JSON.parse(localStorage.getItem("authUser")).token;
        const res = await this.instance.request({
            url: "api/v1/contact",
            headers: { 'Content-Type': 'application/json' },
            method: "get",
            headers: {
                "Authorization": "Token " + token
            }

        });

        return res;
    }

    async updateContact(data) {
        const token = JSON.parse(localStorage.getItem("authUser")).token;
        const res = await this.instance.request({
            url: "api/v1/contact",
            headers: { 'Content-Type': 'application/json' },
            method: "put",
            headers: {
                "Authorization": "Token " + token,
                "Content-Type": "application/json"
            },
            data: data
        });

        return res;
    }

    // about
    async readAbout() {
        const token = JSON.parse(localStorage.getItem("authUser")).token;
        const res = await this.instance.request({
            url: "api/v1/about",
            headers: { 'Content-Type': 'application/json' },
            method: "get",
            headers: {
                "Authorization": "Token " + token
            }

        });

        return res;
    }

    async updateAbout(data) {
        const token = JSON.parse(localStorage.getItem("authUser")).token;
        const res = await this.instance.request({
            url: "api/v1/about",
            headers: { 'Content-Type': 'application/json' },
            method: "put",
            headers: {
                "Authorization": "Token " + token,
                "Content-Type": "application/json"
            },
            data: data
        });

        return res;
    }


    // administrators
    async getAdministrators() {
        const token = JSON.parse(localStorage.getItem("authUser")).token;
        const res = await this.instance.request({
            url: "api/v1/administrators",
            headers: { 'Content-Type': 'application/json' },
            method: "get",
            headers: {
                "Authorization": "Token " + token
            }

        });

        return res;
    }


    // services
    async getServices() {
        const token = JSON.parse(localStorage.getItem("authUser")).token;
        const res = await this.instance.request({
            url: "api/v1/services",
            headers: { 'Content-Type': 'application/json' },
            method: "get",
            headers: {
                "Authorization": "Token " + token
            }
        });

        return res;
    }
}

export default APIClient;