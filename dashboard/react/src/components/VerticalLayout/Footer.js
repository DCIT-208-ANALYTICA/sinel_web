import React from "react";
import { Row, Col, Container } from "reactstrap";

const Footer = () => {
    return (
        <React.Fragment>
            <footer className="footer">
                <Container fluid>
                    <Row>
                        <Col sm={6}>
                            {new Date().getFullYear()} © Sinel Hospital
                        </Col>
                        <Col sm={6}>
                            <div className="text-sm-right d-none d-sm-block">
                                made with <i className="mdi mdi-heart text-danger"></i> by Team Analytica.
                            </div>
                        </Col>
                    </Row>
                </Container>
            </footer>
        </React.Fragment>
    );
};

export default Footer;
