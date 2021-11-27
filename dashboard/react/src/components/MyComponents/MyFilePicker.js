import React from 'react'
import { AvField } from "availity-reactstrap-validation";


export default class MyFilePicker extends React.Component {
    inputRef = React.createRef();

    constructor(props) {
        super(props);
        this.state = { inputValue: null }
    }

    handleFileChange = (v) => {
        const { target: { files } } = v
        const cancel = !files.length;

        if (cancel) return;

        // propagate
        if (this.props.handleFileChange) {
            this.props.handleFileChange(v)
        }

        const newFileName = files[0].name;
        this.setState({ inputValue: newFileName })

    };

    handleClick = (...args) => {
        const input = this.inputRef;

        if (input.current) {
            input.current.click();
        }

    }

    render() {
        const { name, label, placeholder, errorMessage, validate } = this.props;

        return (
            <React.Fragment>
                <div style={{ "display": "none" }} >
                    <input
                        type="file"
                        ref={this.inputRef}
                        onChange={this.handleFileChange}
                        name="file"
                    />
                </div>
                <AvField
                    value={this.state.inputValue}
                    onClick={this.handleClick}
                    readonly="readonly"
                    name={name}
                    label={label}
                    placeholder={placeholder}
                    errorMessage={errorMessage}
                    validate={validate}
                />
            </React.Fragment>
        );
    }
}
