import React, { useEffect, useState } from 'react';
import ReactLoading from "react-loading";
import sleep from '../functions/sleep';
import pageTypes from '../constants/pageTypes';
import getUserData from '../api/getUserData';
import tg_user_id from '../constants/tg_user_id';
import getAds from '../api/getAds';
import getRefs from '../api/getRefs';
import tg_name from '../constants/tg_name';
import tg_image from '../constants/tg_image';

function Loading({ setPage, setUserData, setAds, setRefs, setCoins, startId }) {
    const [adsState, setAdsState] = useState([])
    useEffect(() => {
        getRefs(tg_user_id).then(res => {
            setRefs(res.data.refs)
        })
        getUserData(tg_user_id, tg_name, tg_image).then((res) => {
            setUserData(res.data)
            setCoins(res.data.coins)
            sleep(500).then(_ => {
                setPage(pageTypes.earn)
            })
        })
        console.log('s ',startId);
        getAds(startId).then(res => {
            const adsData = res.data.ads;
            setAdsState(adsData);
        })

    }, [setPage, setUserData, setAds, setRefs, startId, setCoins])

    useEffect(() => {
        setAds(adsState);
    }, [adsState, setAds])

    return (
        <div className='loading'>
            <ReactLoading type='spin' color='#5EB5F7' />
        </div>
    );
}

export default Loading;