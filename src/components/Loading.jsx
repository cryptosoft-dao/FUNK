import React, { useEffect } from 'react';
import ReactLoading from "react-loading";
import sleep from '../functions/sleep';
import pageTypes from '../constants/pageTypes';
import getUserData from '../api/getUserData';
import tg_user_id from '../constants/tg_user_id';
import getAds from '../api/getAds';

function Loading({ setPage, setUserData, setAds }) {
    useEffect(() => {
        getUserData(tg_user_id).then((res) => {
            setUserData(res.data)
            sleep(500).then(_ => {
                setPage(pageTypes.earn)
            })
        })
        getAds().then(res => {
            setAds(res.data.ads)
        })

    }, [setPage, setUserData, setAds])
    return (
        <div className='loading'>
            <ReactLoading type='spin' color='#5EB5F7' />
        </div>
    );
}

export default Loading;