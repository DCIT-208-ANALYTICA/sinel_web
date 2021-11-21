import React, { useEffect } from 'react';
import { useHistory } from 'react-router-dom';

const Logout = () => {
    const history = useHistory();
    useEffect(() => {
        localStorage.removeItem("authUser");
        history.push("/login");
    }, [])


    return (
        <React.Fragment>
            <h1>&nbsp;</h1>
        </React.Fragment>
    );
}

export default Logout

