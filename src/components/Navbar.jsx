import React from 'react';
import { PiBowlSteamFill } from 'react-icons/pi';
import { SiTask } from "react-icons/si";
import pageTypes from '../constants/pageTypes';
import sleep from '../functions/sleep';

function Navbar({ setPage, onPageChangeToEarn }) {
    return (
        <div className='navbar'>
            <div className="navbar__item" onClick={() => { setPage(pageTypes.team) }}>
                <PiBowlSteamFill size={34} />
                <p>Team</p>
            </div>
            <div className="navbar__item" onClick={() => {
                let pageElement = document.querySelector('.page__second')
                pageElement.animate([
                    { 'left': "0%" },
                    { 'left': "100%" },
                ], { 'duration': 500 })
                sleep(450).then(() => {
                    setPage(pageTypes.earn)
                })
            }}>
                <SiTask size={34} />
                <p>Earn</p>
            </div>
            <div className="navbar__item" onClick={() => { setPage(pageTypes.tasks) }}>
                <SiTask size={34} />
                <p>Tasks</p>
            </div>
        </div>
    );
}

export default Navbar;