import React, { useEffect, useState, useContext } from 'react'
import { Row, Col, Card, CardBody, FormGroup, Button, Container, Spinner, Alert, TabContent, TabPane, NavLink, NavItem, CardText, Nav } from "reactstrap";

import Breadcrumbs from '../../components/Common/Breadcrumb';
import { Editor } from "react-draft-wysiwyg";
import { ContentState, EditorState } from 'draft-js';

import { GlobalContext } from '../../store/globalState';
import APIClient from '../../helpers/client';
import classnames from "classnames";


const client = new APIClient();

const About = () => {
    const { globalState, setGlobalState } = useContext(GlobalContext);

    const [breadcrumbItems, setBreadCrumbItems] = useState([
        { title: "Dashboard", link: "#" },
        { title: "About", link: "#" },
    ]);

    const [showSuccess, setShowSuccess] = useState(false);
    const [activeTabJustify, setActiveTabJustify] = useState("5")
    const [about, setAbout] = useState({})
    const [editorState, setEditorState] = useState()

    useEffect(() => {
        const fetchData = async () => {
            try {
                const result = await client.readAbout()
                updateAbout(result);
            } catch (e) {
                console.log("there was an error");
            }
        }
        fetchData()
    }, []);


    // functionality
    const getPlainText = (editorState) => {
        return editorState.getCurrentContent().getPlainText();
    }

    const setupEditorState = (result) => {
        const aboutObj = result.data.about;

        const overviewText = aboutObj.overview;
        const missionText = aboutObj.mission
        const visionText = aboutObj.vision
        const valueText = aboutObj.value

        const newEditorState = {
            overview: EditorState.createWithContent(ContentState.createFromText(overviewText)),
            mission: EditorState.createWithContent(ContentState.createFromText(missionText)),
            vision: EditorState.createWithContent(ContentState.createFromText(visionText)),
            value: EditorState.createWithContent(ContentState.createFromText(valueText))
        };

        setEditorState(newEditorState);
    }

    const toggleCustomJustified = (tab) => {
        if (activeTabJustify !== tab) {
            setActiveTabJustify(tab);

        }
    }
    const onEditorStateChange = (state) => {
        console.log(state);
    }

    const updateAbout = (result) => {
        setGlobalState((prev) => {
            // setup editor state
            setupEditorState(result)
            return { ...prev, about: result.data.about };
        });
    }

    const handleSubmit = async (event) => {
        // validate
        if (false) {
            return
        }

        const payload = {
            "overview": getPlainText(editorState.overview),
            "mission": getPlainText(editorState.mission),
            "vision": getPlainText(editorState.vision),
            "value": getPlainText(editorState.value)
        }


        try {
            const result = await client.updateAbout(payload);
            setShowSuccess(true)
            updateAbout(result);

        } catch (e) {
            console.log("there was an error :(")
        }
    }


    // loading
    if (!globalState.about || !editorState) {
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
                    <Breadcrumbs title="About" breadcrumbItems={breadcrumbItems} />
                    <Alert isOpen={showSuccess} color="success" role="alert">
                        About updated successfully
                    </Alert>
                    <Row>


                        <Col xl={12}>
                            <Card>
                                <CardBody>
                                    <h4 className="card-title">About</h4>
                                    <p className="card-title-desc">
                                        You can edit about information with this form
                                    </p>

                                    <Nav tabs className="nav-tabs-custom nav-justified">
                                        <NavItem>
                                            <NavLink
                                                style={{ cursor: "pointer" }}
                                                className={classnames({
                                                    active: activeTabJustify === "5"
                                                })}
                                                onClick={() => {
                                                    toggleCustomJustified("5");
                                                }}
                                            >
                                                <span className="d-none d-sm-block">Overview</span>
                                            </NavLink>
                                        </NavItem>
                                        <NavItem>
                                            <NavLink
                                                style={{ cursor: "pointer" }}
                                                className={classnames({
                                                    active: activeTabJustify === "6"
                                                })}
                                                onClick={() => {
                                                    toggleCustomJustified("6");
                                                }}
                                            >
                                                <span className="d-none d-sm-block">Mission</span>
                                            </NavLink>
                                        </NavItem>
                                        <NavItem>
                                            <NavLink
                                                style={{ cursor: "pointer" }}
                                                className={classnames({
                                                    active: activeTabJustify === "7"
                                                })}
                                                onClick={() => {
                                                    toggleCustomJustified("7");
                                                }}
                                            >
                                                <span className="d-none d-sm-block">Vision</span>
                                            </NavLink>
                                        </NavItem>
                                        <NavItem>
                                            <NavLink
                                                style={{ cursor: "pointer" }}
                                                className={classnames({
                                                    active: activeTabJustify === "8"
                                                })}
                                                onClick={() => {
                                                    toggleCustomJustified("8");
                                                }}
                                            >
                                                <span className="d-none d-sm-block">Value</span>
                                            </NavLink>
                                        </NavItem>
                                    </Nav>

                                    <TabContent activeTab={activeTabJustify}>
                                        <TabPane tabId="5" className="p-3">
                                            <Row>
                                                <Col sm="12">
                                                    <Editor
                                                        editorState={editorState.overview}
                                                        toolbarClassName="toolbarClassName"
                                                        wrapperClassName="wrapperClassName"
                                                        editorClassName="editorClassName"
                                                        onEditorStateChange={(state) => {
                                                            setEditorState((prev) => ({ ...prev, overview: state }))
                                                        }}
                                                    />
                                                </Col>
                                                <Col>
                                                    <FormGroup className="mt-3">
                                                        <div>
                                                            <Button onClick={handleSubmit} type="submit" color="primary" className="mr-1">
                                                                Save
                                                            </Button>
                                                        </div>
                                                    </FormGroup>
                                                </Col>
                                            </Row>

                                        </TabPane>
                                        <TabPane tabId="6" className="p-3">
                                            <Row>
                                                <Col sm="12">
                                                    <Editor
                                                        editorState={editorState.mission}
                                                        toolbarClassName="toolbarClassName"
                                                        wrapperClassName="wrapperClassName"
                                                        editorClassName="editorClassName"
                                                        onEditorStateChange={(state) => {
                                                            setEditorState((prev) => ({ ...prev, mission: state }))
                                                        }}
                                                    />
                                                </Col>
                                                <Col>
                                                    <FormGroup className="mt-3">
                                                        <div>
                                                            <Button onClick={handleSubmit} type="submit" color="primary" className="mr-1">
                                                                Save
                                                            </Button>
                                                        </div>
                                                    </FormGroup>
                                                </Col>
                                            </Row>
                                        </TabPane>
                                        <TabPane tabId="7" className="p-3">
                                            <Row>
                                                <Col sm="12">
                                                    <Editor
                                                        editorState={editorState.vision}
                                                        toolbarClassName="toolbarClassName"
                                                        wrapperClassName="wrapperClassName"
                                                        editorClassName="editorClassName"
                                                        onEditorStateChange={(state) => {
                                                            setEditorState((prev) => ({ ...prev, vision: state }))
                                                        }}
                                                    />
                                                </Col>
                                                <Col>
                                                    <FormGroup className="mt-3">
                                                        <div>
                                                            <Button onClick={handleSubmit} type="submit" color="primary" className="mr-1">
                                                                Save
                                                            </Button>
                                                        </div>
                                                    </FormGroup>
                                                </Col>
                                            </Row>
                                        </TabPane>

                                        <TabPane tabId="8" className="p-3">
                                            <Row>
                                                <Col sm="12">
                                                    <Editor
                                                        editorState={editorState.value}
                                                        toolbarClassName="toolbarClassName"
                                                        wrapperClassName="wrapperClassName"
                                                        editorClassName="editorClassName"
                                                        onEditorStateChange={(state) => {
                                                            setEditorState((prev) => ({ ...prev, value: state }))
                                                        }}
                                                    />
                                                </Col>
                                                <Col>
                                                    <FormGroup className="mt-3">
                                                        <div>
                                                            <Button onClick={handleSubmit} type="submit" color="primary" className="mr-1">
                                                                Save
                                                            </Button>
                                                        </div>
                                                    </FormGroup>
                                                </Col>
                                            </Row>
                                        </TabPane>
                                    </TabContent>
                                </CardBody>
                            </Card>
                        </Col>




                    </Row>
                </Container>
            </div>
        </React.Fragment>
    );
}

export default About;