import React, { useEffect, useState } from 'react';
import BASE_URL from '../constants/BASE_URL';
import { useSwipeable } from 'react-swipeable';
import { FaExternalLinkAlt } from "react-icons/fa";
import { IoIosShareAlt } from "react-icons/io";
import { PiUsersThreeFill } from "react-icons/pi";

function Earn({ setPage, userData, ads, defaultAdIndex = 1 }) {
    const [animationDuration] = useState(100)
    const [adIndex, setAdIndex] = useState(defaultAdIndex)
    const [ad, setAd] = useState(ads[adIndex])
    const [img1Src, setImg1Src] = useState('')
    const [img2Src, setImg2Src] = useState('')

    const swipingHandler = (eventData) => {
        console.log(eventData);
        console.log(ads.length, adIndex);
        if (adIndex + 1 >= ads.length) {
            setAdIndex(0)
        }
        else {
            setAdIndex(adIndex + 1)
        }
    }
    const openHandler = () => {
        window.open(ad.url, '_blank')
    }

    const swipe = useSwipeable({
        onSwipedLeft: swipingHandler,
        delta: 30,                             // min distance(px) before a swipe starts. *See Notes*
        preventScrollOnSwipe: false,           // prevents scroll during swipe (*See Details*)
        trackTouch: true,                      // track touch input
        trackMouse: false,                     // track mouse input
        rotationAngle: 0,                      // set a rotation angle
        swipeDuration: Infinity,               // allowable duration of a swipe (ms). *See Notes*
        touchEventOptions: { passive: true },  // options for touch listeners (*See Details*) 
    })
    useEffect(() => {
        setAd(ads[adIndex])
    }, [adIndex, ads])
    useEffect(() => {
        setImg1Src(`${BASE_URL}${ad.image}`)
        if (adIndex === 0) {
            setImg2Src(`${BASE_URL}${ads[ads.length - 1].image}`)
        }
        else {
            setImg2Src(`${BASE_URL}${ads[adIndex - 1].image}`)
        }
    }, [ad, adIndex, ads])
    useEffect(() => {
        const nextImage = document.querySelector('.now_image')
        nextImage.animate([
            { 'left': "100%" },
            { 'left': "0%" },
        ], { 'duration': animationDuration })
    }, [img2Src, animationDuration])
    useEffect(() => {
        const nowImage = document.querySelector('.next_image')
        nowImage.animate([
            { 'left': "0%" },
            { 'left': "-100%" },
        ], { 'duration': animationDuration })
    }, [img1Src, animationDuration])
    console.log(ad, ads, adIndex);
    return (
        <div className="earn_screen" {...swipe}>
            <div className="up">
                <h1>FUNK</h1>
            </div>
            <img className='ad_image now_image' src={img1Src} alt="" />
            <img className='next_image' src={img2Src} alt="" />
            <div className="down">
                <div className="inner inner__1" style={{ margin: 12 }}>
                    <button onClick={openHandler} className="btn" style={ad.url === '' ? { 'opacity': 0, 'visibility': 'hidden' } : {}}>Visit site <FaExternalLinkAlt size={26} /></button>
                    <h4 className='points'>9999</h4>
                </div>
                <div className="inner inner__2" style={{ margin: 12, marginBottom: 0 }}>
                    <div className="inner__2_item inner__2_item_1">
                        <div className="title">{ad.name}</div>
                        <div className="desc">{ad.description}</div>
                    </div>
                    <div className="inner__2_item inner__2_item_2">
                        <div className="icon"><IoIosShareAlt size={"70%"} /></div>
                        <div className="icon"><PiUsersThreeFill size={"70%"} /></div>

                    </div>
                </div>
            </div>
        </div>
    );
}

export default Earn;