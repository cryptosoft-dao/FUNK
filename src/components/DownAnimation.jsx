import React, { useEffect, useState } from 'react';
import sleep from '../functions/sleep';

function DownAnimation({ x, y }) {
    const [show, setShow] = useState(true)
    useEffect(() => {
        sleep(950).then(_=>{
            setShow(false)
        })
    }, [])
    return (
        <>
            {show && (
                <div className='down_animation' style={{ left: x, top: y }}></div>
            )}
        </>

    );
}

export default DownAnimation;