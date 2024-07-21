import React from 'react';
import { IoChevronBack } from 'react-icons/io5';
import sleep from '../functions/sleep';
import pageTypes from '../constants/pageTypes';
import convertCoins from '../functions/convertCoins';
import { FaUser } from "react-icons/fa";
import tg_name from '../constants/tg_name';

function Team({ setPage, refs }) {

    const backHandler = () => {
        let pageElement = document.querySelector('.page__second')
        pageElement.animate([
            { 'left': "0%" },
            { 'left': "100%" },
        ], { 'duration': 500, 'easing': 'ease-in' })
        sleep(470).then(() => {
            setPage(pageTypes.earn)
        })
    }
    return (
        <div className='page__second page team'>
            <div className="line">
                <IoChevronBack style={{ cursor: "pointer" }} size={48} onClick={backHandler} />
                <h1>Team</h1>
            </div>
            {refs.map((value, idx) => (
                <div className="line ref" key={idx}>
                    <div className="inner_1">
                        <div className="img">
                            <FaUser size={24} color='#000' />
                        </div>
                        <div className="text">
                            <div className="title">{value.name}</div>
                            <div className="frends_count">{value.total_friends === 1 ? `${value.total_friends} friend` : `${value.total_friends} friends`}</div>
                        </div>
                    </div>
                    <div className="inner_2">
                        <div className="coins">{convertCoins(value.money)}</div>
                    </div>
                </div>
            ))}
            {refs.length === 0 && (
                <h2 style={{ 'width': '100%', textAlign: 'center', paddingTop: 100 }}>😭 You haven't anyone yet 😭</h2>
            )}
            <div style={{ height: 300 }}></div>
        </div>
    );
}
//<div className="img">
//   <img src={`https://ui-avatars.com/api/?name=${value.name}&length=2&size=40&font-size=0.8&color=000000`} alt="" />
//</div>
export default Team;