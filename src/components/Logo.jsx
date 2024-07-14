import React from 'react';
import letter from '../constants/letter';

function Logo({ letterText = null }) {
    return (
        <div className='logo'>
            <h1>{letterText == null ? letter : letterText}</h1>
        </div>
    );
}

export default Logo;