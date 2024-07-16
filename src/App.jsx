import { useEffect, useState } from "react";
import Earn from "./pages/Earn";
import pageTypes from "./constants/pageTypes";
import Loading from "./components/Loading";
import Team from "./pages/Team";

function App() {
  const [userData, setUserData] = useState({})
  const [defaultAdIndex, setDefaultAdIndex] = useState(1)
  const [ads, setAds] = useState({})
  const [page, setPage] = useState(pageTypes.loading)

  useEffect(() => {
    let ID = window.location.pathname.split('/')[1]
    if (ID === ''){
      ID = 0
    }
    else{
      ID = Number(ID)
    }
    setDefaultAdIndex(ID)
  }, [])

  return (
    <>
      {page === pageTypes.loading && (<Loading setUserData={setUserData} setPage={setPage} setAds={setAds} />)}
      {page !== pageTypes.loading && (<Earn userData={userData} setPage={setPage} ads={ads} defaultAdIndex={defaultAdIndex} />)}
      {page === pageTypes.team && (<Team setPage={setPage} />)}
    </>
  );
}
//{page !== pageTypes.loading && (<Navbar setPage={setPage} />)}
//w480 h853
export default App;
