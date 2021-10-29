import React, { useState, useEffect } from "react";
export const GlobalContext = React.createContext({ gloablState: null, setGlobalState: null });

export function MyGlobalProvider({ children }) {
    const [globalState, setGlobalState] = useState({});

    return <GlobalContext.Provider value={{ globalState, setGlobalState }}>
        {children}
    </GlobalContext.Provider>
}