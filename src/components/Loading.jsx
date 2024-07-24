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
        (async () => {
            let res = await getRefs(tg_user_id)
            setRefs(res.data.refs)

            let res2 = await getUserData(tg_user_id, tg_name, tg_image)
            setUserData(res2.data)
            setCoins(res2.data.coins)

            let res3 = await getAds(startId)
            const adsData = res3.data.ads;
            console.log(adsData);
            setAdsState(adsData);
            setAds(adsData)
            await sleep(500)
            setPage(pageTypes.earn)
        })()
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