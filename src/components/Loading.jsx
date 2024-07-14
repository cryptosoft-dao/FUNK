import React, { useEffect } from 'react';
import ReactLoading from "react-loading";
import sleep from '../functions/sleep';
import pageTypes from '../constants/pageTypes';

function Loading({ setPage }) {
    useEffect(() => {
        sleep(2000).then(_ => {
            setPage(pageTypes.earn)
        })
    }, [setPage])
    return (
        <div className='loading'>
            <ReactLoading type='spin' color='#5EB5F7' />
        </div>
    );
}

export default Loading;