import React, { useEffect, useState, useContext } from 'react'
import { Row, Col, Card, CardBody, FormGroup, Button, Container, Spinner, Alert } from "reactstrap";

import { AvForm, AvField, AvInput } from "availity-reactstrap-validation";
//Import Breadcrumb
import Breadcrumbs from '../../components/Common/Breadcrumb';

import { GlobalContext } from '../../store/globalState';
import APIClient from '../../helpers/client';


const client = new APIClient();

const Contact = () => {
    const { globalState, setGlobalState } = useContext(GlobalContext);

    const [breadcrumbItems, setBreadCrumbItems] = useState([
        { title: "Dashboard", link: "#" },
        { title: "Contact", link: "#" },
    ]);

    const [showSuccess, setShowSuccess] = useState(false);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const result = await client.getContact()
                updateContact(result);

            } catch (e) {
                console.log("there was an error");
            }
        }
        fetchData()
    }, []);


    // functionality
    const updateContact = (result) => {
        setGlobalState((prev) => ({ ...prev, contact: result.data.contact }));
    }

    const handleSubmit = async (event, errors, values) => {
        if (errors.length) {
            return
        }

        try {
            const payload = {
                "gps": values.gps,
                "email": values.email,
                "address": values.address,
                "telephone": values.telephone,
                "lat_lng": values.latlng
            }

            const result = await client.updateContact(payload);
            setShowSuccess(true)
            updateContact(result);
            console.log(result);

        } catch (e) {
            console.log("there was an error :(")
        }
    }


    // loading
    if (!globalState.contact) {
        return (
            <div className="page-content">
                <div style={{ display: "block" }}>
                    <div style={{ margin: "0 auto", width: 60 }}>
                        <Spinner className="mr-2" color="dark" />
                    </div>
                </div>
            </div>
        );
    }
    const contact = globalState.contact;

    return (
        <React.Fragment>
            <div className="page-content">
                <Container fluid={true}>
                    <Breadcrumbs title="Contact" breadcrumbItems={breadcrumbItems} />
                    <Alert isOpen={showSuccess} color="success" role="alert">
                        Contact updated successfully
                    </Alert>
                    <Row>
                        <Col lg={12}>
                            <Card>
                                <CardBody>
                                    <h4 className="card-title">Contact Information</h4>
                                    <p className="card-title-desc">
                                        You can edit contact information with this form.
                                    </p>

                                    <AvForm onSubmit={handleSubmit}>
                                        <AvField
                                            name="email"
                                            label="Email"
                                            placeholder="Type Something"
                                            type="email"
                                            errorMessage="Enter email"
                                            value={contact.email}
                                            validate={{ required: { value: true }, email: { value: true } }}
                                        />
                                        <AvField
                                            name="gps"
                                            label="Gps"
                                            type="text"
                                            placeholder="Gps"
                                            errorMessage="Enter gps"
                                            value={contact.gps}
                                            validate={{ required: { value: true } }}
                                        />

                                        <AvField
                                            name="address"
                                            label="Address"
                                            placeholder="Enter address"
                                            type="text"
                                            errorMessage="Invalid email"
                                            value={contact.address}
                                            validate={{
                                                required: { value: true },
                                            }}
                                        />

                                        <AvField
                                            name="telephone"
                                            label="Telephone"
                                            placeholder="Enter telephone"
                                            type="text"
                                            errorMessage="Invalid telephone"
                                            value={contact.telephone}
                                            validate={{
                                                required: { value: true },
                                            }}
                                        />

                                        <AvField
                                            name="latlng"
                                            label="Location (latlng)"
                                            placeholder="Enter location"
                                            type="text"
                                            errorMessage="Invalid location"
                                            value={contact.lat_lng}
                                            validate={{
                                                required: { value: true },
                                            }}
                                        />

                                        <FormGroup className="mb-0">
                                            <div>
                                                <Button type="submit" color="primary" className="mr-1">
                                                    Save
                                                </Button>{" "}
                                                <Button type="reset" color="secondary">
                                                    Cancel
                                                </Button>
                                            </div>
                                        </FormGroup>
                                    </AvForm>
                                </CardBody>
                            </Card>
                        </Col>

                    </Row>
                </Container>
            </div>
        </React.Fragment>
    );
}

export default Contact;