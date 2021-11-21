import React, { useEffect, useState } from 'react';
import APIClient from '../../helpers/client';

// Redux
import { Link } from 'react-router-dom';

import { Row, Col, Input, Button, Container, Label, FormGroup, UncontrolledAlert } from "reactstrap";

// availity-reactstrap-validation
import { AvForm, AvField } from 'availity-reactstrap-validation';

// import images
import logodark from "../../assets/images/logo-dark.png";
import { useHistory } from 'react-router-dom';

const client = new APIClient();

const Login = () => {
    const history = useHistory();
    const [showError, setShowError] = useState(false)
    const [errorMessage, setErrorMessage] = useState("");

    useEffect(() => {
        document.body.classList.add("auth-body-bg");
        return () => {
            document.body.classList.remove("auth-body-bg");
        }
    }, [])

    const handleSubmit = async (event, errors, values) => {
        if (errors.length) {
            return
        }

        const response = await client.login({ email: values.username, password: values.password });
        console.log(response);
        // error
        if (response.data.response.error_message) {
            setErrorMessage(response.data.response.error_message)
            setShowError(true)

        } else {
            // success
            console.log("success")
            localStorage.setItem("authUser", JSON.stringify(response.data.response))
            history.push("/dashboard")
        }

    }


    return (
        <React.Fragment>
            <div className="home-btn d-none d-sm-block">
                <Link to="/"><i className="mdi mdi-home-variant h2 text-white"></i></Link>
            </div>

            <div>
                <Container fluid className="p-0">
                    <Row className="no-gutters">
                        <Col lg={4}>
                            <div className="authentication-page-content p-4 d-flex align-items-center min-vh-100">
                                <div className="w-100">
                                    <Row className="justify-content-center">
                                        <Col lg={9}>
                                            <div>
                                                <div className="text-center">

                                                    {showError ? <UncontrolledAlert color="danger" className="alert-dismissible fade show" role="alert">
                                                        <i className="mdi mdi-block-helper mr-2"></i>
                                                        {errorMessage}
                                                    </UncontrolledAlert> : ""}

                                                    <h4 className="font-size-18 mt-4">Welcome Back !</h4>
                                                    <p className="text-muted">Sign in to continue</p>
                                                </div>


                                                <div className="p-2 mt-5">
                                                    <AvForm onSubmit={handleSubmit} className="form-horizontal" >

                                                        <FormGroup className="auth-form-group-custom mb-4">
                                                            <i className="ri-user-2-line auti-custom-input-icon"></i>
                                                            <Label htmlFor="username">Username</Label>
                                                            <AvField name="username" type="text" className="form-control" id="username" validate={{ email: true, required: true }} placeholder="Enter username" />
                                                        </FormGroup>

                                                        <FormGroup className="auth-form-group-custom mb-4">
                                                            <i className="ri-lock-2-line auti-custom-input-icon"></i>
                                                            <Label htmlFor="userpassword">Password</Label>
                                                            <AvField name="password" type="password" className="form-control" id="userpassword" validate={{ required: true }} placeholder="Enter password" />
                                                        </FormGroup>

                                                        <div className="custom-control custom-checkbox">
                                                            <Input type="checkbox" className="custom-control-input" id="customControlInline" />
                                                            <Label className="custom-control-label" htmlFor="customControlInline">Remember me</Label>
                                                        </div>

                                                        <div className="mt-4 text-center">
                                                            <Button color="primary" className="w-md waves-effect waves-light" type="submit">Log In</Button>
                                                        </div>

                                                        <div className="mt-4 text-center">
                                                            <Link to="/auth-recoverpw" className="text-muted"><i className="mdi mdi-lock mr-1"></i> Forgot your password?</Link>
                                                        </div>
                                                    </AvForm>
                                                </div>

                                            </div>

                                        </Col>
                                    </Row>
                                </div>
                            </div>
                        </Col>
                        <Col lg={8}>
                            <div className="authentication-bg">
                                <div className="bg-overlay"></div>
                            </div>
                        </Col>
                    </Row>
                </Container>
            </div>
        </React.Fragment>
    );
}

export default Login;

