import React, { useEffect, useState, useContext } from 'react'
import { Row, Col, Card, CardBody, Button, Container, Spinner, Table, CardImg, Modal, ModalHeader, ModalBody, ModalFooter, FormGroup } from "reactstrap";

import { AvForm, AvField } from "availity-reactstrap-validation";

import Breadcrumbs from '../../components/Common/Breadcrumb';
import { GlobalContext } from '../../store/globalState';
import APIClient from '../../helpers/client';

import MyMaxChar from '../../components/MyComponents/MyMaxChar';
import MyDropDownButton from '../../components/MyComponents/MyDropDownButton';
import MyFilePicker from '../../components/MyComponents/MyFilePicker';

const client = new APIClient();

const Services = () => {
    const { globalState, setGlobalState } = useContext(GlobalContext);

    const [breadcrumbItems, setBreadCrumbItems] = useState([
        { title: "Dashboard", link: "#" },
        { title: "Services", link: "#" },
    ]);

    const [isModalOpened, setIsModalOpened] = useState(false)
    const [file, setFile] = useState()

    useEffect(() => {
        const fetchData = async () => {
            try {
                const result = await client.getServices()
                updateServices(result);
                console.log(result)

            } catch (e) {
                console.log("there was an error");
            }
        }
        fetchData()
    }, []);


    // functionality
    const updateServices = (result) => {
        setGlobalState((prev) => ({ ...prev, services: result.data.services }));
    }

    const removeBodyCss = () => {
        document.body.classList.add("no_padding");
    }

    const toggleModal = () => {
        setIsModalOpened(!isModalOpened)
        removeBodyCss();
    }

    const onFileChanged = (file) => {
        console.log("file has been changed...");
    }

    const handleSubmit = async (event, errors, values) => {
        if (errors.length) {
            return
        }

        // try {
        //     const payload = {
        //         "gps": values.gps,
        //         "email": values.email,
        //         "address": values.address,
        //         "telephone": values.telephone,
        //         "lat_lng": values.latlng
        //     }

        //     const result = await client.updateContact(payload);
        //     setShowSuccess(true)
        //     updateContact(result);
        //     console.log(result);

        // } catch (e) {
        //     console.log("there was an error :(")
        // }
    }


    // loading
    if (!globalState.services) {
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
    const tableData = globalState.services;

    return (
        <React.Fragment>
            <div className="page-content">
                <Container fluid={true}>
                    <Breadcrumbs title="Services" breadcrumbItems={breadcrumbItems} />

                    <Row>
                        <Col lg={12}>
                            <Card>
                                <CardBody>
                                    <h4 className="card-title">Services</h4>
                                    <p className="card-title-desc">
                                        You can edit services information with this form
                                    </p>

                                    <Button onClick={toggleModal} color="primary" type="button" className="waves-effect waves-light mr-1 mb-4">
                                        Add <i className="ri-add-box-line align-middle ml-2"></i>
                                    </Button>

                                    <Modal
                                        isOpen={isModalOpened}
                                        toggle={toggleModal}
                                    >
                                        <ModalHeader toggle={toggleModal}>
                                            Add Service
                                        </ModalHeader>
                                        <ModalBody>
                                            <AvForm onSubmit={handleSubmit}>
                                                <MyFilePicker
                                                    name="image"
                                                    label="image"
                                                    placeholder="Select a file"
                                                    errorMessage="Please select a file"
                                                    handleFileChange={onFileChanged}
                                                    validate={{ required: { value: true } }}
                                                />
                                                <AvField
                                                    name="gps"
                                                    label="Gps"
                                                    type="text"
                                                    placeholder="Gps"
                                                    errorMessage="Enter gps"
                                                    validate={{ required: { value: true } }}
                                                />

                                                <AvField
                                                    name="address"
                                                    label="Address"
                                                    placeholder="Enter address"
                                                    type="text"
                                                    errorMessage="Invalid email"
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
                                        </ModalBody>
                                        <ModalFooter>
                                            <Button
                                                type="button"
                                                onClick={toggleModal}
                                                color="light"
                                                className="waves-effect"
                                            >
                                                Close
                                            </Button>
                                            <Button
                                                type="button"
                                                color="primary" className="waves-effect waves-light"
                                            >
                                                Add
                                            </Button>
                                        </ModalFooter>
                                    </Modal>

                                    <div className="table-responsive">
                                        <Table className="mb-0">

                                            <thead>
                                                <tr>
                                                    <th>#</th>
                                                    <th>Image</th>
                                                    <th>Title</th>
                                                    <th>Description</th>
                                                    <th>Visible</th>
                                                    <th>Actions</th>
                                                </tr>
                                            </thead>
                                            <tbody>

                                                {tableData.map((cur, index) => {
                                                    return <tr>
                                                        <th scope="row">{index + 1}</th>
                                                        <td>
                                                            <CardImg src={cur.image ?? "https://uifaces.co/wp-content/themes/uifaces-theme/src/img/home-animation/avatar-3.svg"} alt="Nazox" className="rounded avatar-sm" />
                                                        </td>
                                                        <td>{<MyMaxChar text={cur.title} charLen={20} />}</td>
                                                        <td>{<MyMaxChar text={cur.description} charLen={50} />}</td>
                                                        <td>{cur.visible ? "Yes" : "No"}</td>
                                                        <td>
                                                            <MyDropDownButton title="Actions" items={
                                                                [
                                                                    { title: "Edit", callback: () => { } },
                                                                    { title: "Delete", callback: () => { } },
                                                                ]} />
                                                        </td>
                                                    </tr>;
                                                })}

                                            </tbody>
                                        </Table>
                                    </div>

                                </CardBody>
                            </Card>
                        </Col>

                    </Row>
                </Container>
            </div>
        </React.Fragment>
    );
}

export default Services;

