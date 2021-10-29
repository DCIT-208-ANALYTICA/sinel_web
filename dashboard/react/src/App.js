import React, { Component } from "react";
import { Switch, BrowserRouter as Router } from "react-router-dom";
import { connect } from "react-redux";

// Import Routes
import { authProtectedRoutes, publicRoutes } from "./routes/";
import AppRoute from "./routes/route";

// layouts
import VerticalLayout from "./components/VerticalLayout/";
import HorizontalLayout from "./components/HorizontalLayout/";
import NonAuthLayout from "./components/NonAuthLayout";

// Import scss
import "./theme.scss";
import { MyGlobalProvider } from "./store/globalState";


class App extends Component {
	constructor(props) {
		super(props);
		this.state = {};
		this.getLayout = this.getLayout.bind(this);
	}

	/**
   * Returns the layout
   */
	getLayout = () => {
		let layoutCls = VerticalLayout;

		switch (this.props.layout.layoutType) {
			case "horizontal":
				layoutCls = HorizontalLayout;
				break;
			default:
				layoutCls = VerticalLayout;
				break;
		}

		return layoutCls;
	};

	render() {
		const Layout = this.getLayout();

		return (
			<React.Fragment>
				<MyGlobalProvider>
					<Router>
						<Switch>
							{publicRoutes.map((route, idx) => (
								<AppRoute
									path={route.path}
									layout={NonAuthLayout}
									component={route.component}
									key={idx}
									isAuthProtected={false}
								/>
							))}

							{authProtectedRoutes.map((route, idx) => (
								<AppRoute
									path={route.path}
									layout={Layout}
									component={route.component}
									key={idx}
									isAuthProtected={true}
								/>
							))}
						</Switch>
					</Router>
				</MyGlobalProvider>
			</React.Fragment>
		);
	}
}

const mapStateToProps = state => {
	return {
		layout: state.Layout
	};
};


export default connect(mapStateToProps, null)(App);
