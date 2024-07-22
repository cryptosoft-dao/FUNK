import { useEffect, useState } from "react";
import Earn from "./pages/Earn";
import pageTypes from "./constants/pageTypes";
import Loading from "./components/Loading";
import Team from "./pages/Team";
import swipeUser from "./api/swipeUser";
import tg_user_id from "./constants/tg_user_id";

function App() {
  const [userData, setUserData] = useState({})
  const [defaultAdIndex, setDefaultAdIndex] = useState(-1)
  const [ads, setAds] = useState({})
  const [page, setPage] = useState(pageTypes.loading)
  const [refs, setRefs] = useState([])
  const [coins, setCoins] = useState(0)

  const swipeHandler = async () => {
    setCoins(coins + 1)
    let res = await swipeUser(tg_user_id)
    setCoins(res.data.coins)
  }

  useEffect(() => {
    let ID = window.location.href.split('?')[1]
    if (!ID) { ID = 0 }
    if (ID === '') {
      ID = 0
    }
    else {
      ID = Number(ID)
    }
    setDefaultAdIndex(ID)
    console.log(ID);
  }, [])

  return (
    <>
      {page === pageTypes.loading && defaultAdIndex !== -1 && (<Loading startId={defaultAdIndex} setCoins={setCoins} setUserData={setUserData} setPage={setPage} setAds={setAds} setRefs={setRefs} />)}
      {page !== pageTypes.loading && (<Earn swipeHandler={swipeHandler} coins={coins} userData={userData} setPage={setPage} ads={ads} />)}
      {page === pageTypes.team && (<Team setPage={setPage} refs={refs} />)}
    </>
  );
}
//{page !== pageTypes.loading && (<Navbar setPage={setPage} />)}
//w480 h853
export default App;
