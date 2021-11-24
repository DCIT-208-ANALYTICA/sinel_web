import React, { Component,useState } from "react";
import { useHistory } from 'react-router-dom';
import axios from "axios";
import { Row, Col, Button, Alert, Container, Label, FormGroup } from "reactstrap";

// availity-reactstrap-validation
import { AvForm, AvField } from "availity-reactstrap-validation";

// action
import {  registerUser, registerUserFailed, apiError } from '../../store/actions';

// Redux
import { connect } from "react-redux";
import { Link } from "react-router-dom";

// import images
import logodark from "../../assets/images/logo-dark.png";

const Register =()=>{
  const history = useHistory();
  const  [email, setEmail]= useState("");
  const [password, setPassword] = useState("");
  const [username, setUsername]= useState("");
  const [register, setRegister] = useState(false)


  const handleUserInput = (event) => {
    setUsername(event.target.value);
  };

  const handleEmailInput = (event) => {
    setEmail(event.target.value);
  };

  const handlePasswordInput = (event) => {
    setPassword(event.target.value);
  };

 
 const handleSubmit = (event) =>{
     event.preventDefault()
     const newUser ={
         email:email,
         password:password,
         username:username,
     }
     console.log(newUser)
     console.log("try again");
    axios.post("http://127.0.0.1:8000/api/v1/administrators/register/" , newUser)
    .then((res)=>{
        console.log("success");
        if (res.status === 200) {
            localStorage.setItem("register", true);
            history.push("/login");
          }
        })
        .catch((err) => {
          console.log(err);
    })
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
                                                <div>
                                                    <Link to="#" className="logo"><img src={logodark} height="20" alt="logo"/></Link>
                                                </div>
    
                                                <h4 className="font-size-18 mt-4">Register account</h4>
                                                <p className="text-muted">Get your free Nazox account now.</p>
                                            </div>

                                           
                                            <div className="p-2 mt-5">
                                                <AvForm onSubmit={handleSubmit} className="form-horizontal" >

                                                    <FormGroup className="auth-form-group-custom mb-4">
                                                        <i className="ri-mail-line auti-custom-input-icon"></i>
                                                        <Label htmlFor="useremail">Email</Label>
                                                        <AvField name="email"  value={email} validate={{email: true, required: true}} onChange={handleEmailInput} type="email" className="form-control" id="useremail" placeholder="Enter email"/>
                                                    </FormGroup>
                    
                                                    <FormGroup className="auth-form-group-custom mb-4">
                                                        <i className="ri-user-2-line auti-custom-input-icon"></i>
                                                        <Label htmlFor="username">Username</Label>
                                                        <AvField name="username"  value={username} type="text" onChange={handleUserInput} className="form-control" id="username" placeholder="Enter username"/>
                                                    </FormGroup>
                            
                                                    <FormGroup className="auth-form-group-custom mb-4">
                                                        <i className="ri-lock-2-line auti-custom-input-icon"></i>
                                                        <Label htmlFor="userpassword">Password</Label>
                                                        <AvField name="password"  value={password} type="password" onChange={handlePasswordInput} className="form-control" id="userpassword" placeholder="Enter password"/>
                                                    </FormGroup>
                            

                                                    <div className="text-center">
                                                        <Button color="primary" className="w-md waves-effect waves-light" type="submit">Register</Button>
                                                    </div>

                                                    <div className="mt-4 text-center">
                                                        <p className="mb-0">By registering you agree to the Nazox <Link to="#" className="text-primary">Terms of Use</Link></p>
                                                    </div>
                                                </AvForm>
                                            </div>

                                            <div className="mt-5 text-center">
                                                <p>Already have an account ? <Link to="/login" className="font-weight-medium text-primary"> Login</Link> </p>
                                                <p>© 2020 Nazox. Crafted with <i className="mdi mdi-heart text-danger"></i> by Themesdesign</p>
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




export default Register;
