import React, { useState } from 'react'
import { DropdownMenu, DropdownItem, DropdownToggle, ButtonDropdown } from "reactstrap";

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

export default MyDropDownButton;