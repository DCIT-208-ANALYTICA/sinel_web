const MyMaxChar = ({ text, charLen = 1000 }) => {
    if (text.length > charLen) {
        return text.slice(0, charLen) + " " + "...";
    }

    return text;
}

export default MyMaxChar;