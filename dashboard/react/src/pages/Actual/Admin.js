import React, { useEffect, useState, useContext } from 'react'
import {
    Row, Col, Card, CardBody, FormGroup, Button, Container, Spinner, Alert, Table, DropdownMenu, DropdownItem, DropdownToggle, ButtonDropdown, CardImg

} from "reactstrap";

import { AvForm, AvField, AvInput } from "availity-reactstrap-validation";

//Import Breadcrumb
import Breadcrumbs from '../../components/Common/Breadcrumb';

import { GlobalContext } from '../../store/globalState';
import APIClient from '../../helpers/client';

import avatar3 from "../../assets/images/users/avatar-3.jpg";


const client = new APIClient();

const Admin = () => {
    const { globalState, setGlobalState } = useContext(GlobalContext);

    const [breadcrumbItems, setBreadCrumbItems] = useState([
        { title: "Dashboard", link: "#" },
        { title: "Admin", link: "#" },
    ]);

    const [showSuccess, setShowSuccess] = useState(false);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const result = await client.getAdministrators()
                updateAdministrators(result);
                console.log(result)

            } catch (e) {
                console.log("there was an error");
            }
        }
        fetchData()
    }, []);


    // functionality
    const updateAdministrators = (result) => {
        setGlobalState((prev) => ({ ...prev, administrators: result.data.administrators }));
    }

    // loading
    if (!globalState.administrators) {
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
    const tableData = globalState.administrators;

    return (
        <React.Fragment>
            <div className="page-content">
                <Container fluid={true}>
                    <Breadcrumbs title="Administrators" breadcrumbItems={breadcrumbItems} />
                    {/* <Alert isOpen={showSuccess} color="success" role="alert">
                        Contact updated successfully
                    </Alert> */}

                    <Row>
                        <Col lg={12}>
                            <Card>
                                <CardBody>
                                    <h4 className="card-title">Administrators</h4>
                                    <p className="card-title-desc">
                                        You can edit about information with this form
                                    </p>

                                    <div className="table-responsive">
                                        <Table className="mb-0">

                                            <thead>
                                                <tr>
                                                    <th>#</th>
                                                    <th>Photo</th>
                                                    <th>Full Name</th>
                                                    <th>Email</th>
                                                    <th>Super Admin</th>
                                                    <th>Actions</th>
                                                </tr>
                                            </thead>
                                            <tbody>

                                                {tableData.map((cur, index) => {
                                                    return <tr>
                                                        <th scope="row">{index + 1}</th>
                                                        <td>
                                                            <CardImg src={cur.photo ?? "https://uifaces.co/wp-content/themes/uifaces-theme/src/img/home-animation/avatar-3.svg"} alt="Nazox" className="rounded-circle avatar-sm" />
                                                        </td>
                                                        <td>{cur.fullname}</td>
                                                        <td>{cur.email_address}</td>
                                                        <td>{cur.is_superuser ? "Yes" : "No"}</td>
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

export default Admin;


const MyDropDownButton = (
    {
        title = "DropDown",
        items = [
            { title: "One", callback: () => { } },
            { title: "Two", callback: () => { } },
        ]
    }) => {
    const [isOpen, setIsOpen] = useState(false);

    return (
        <ButtonDropdown
            isOpen={isOpen}
            toggle={() => setIsOpen(!isOpen)}
        >
            <DropdownToggle caret color="light">
                {title} <i className="mdi mdi-chevron-down"></i>
            </DropdownToggle>
            <DropdownMenu>
                {items.map((cur) => <DropdownItem onClick={cur.callback} >{cur.title}</DropdownItem>)}
            </DropdownMenu>
        </ButtonDropdown>
    );
}