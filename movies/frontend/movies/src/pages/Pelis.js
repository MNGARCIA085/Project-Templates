
import axios from "axios";
import React from "react";
import PelisList from '../components/PelisList';

const Pelis = () => {

    const baseURL = 'http://127.0.0.1:8000/API/movies/';


      const [pelis, setPelis] = React.useState(null);

        React.useEffect(() => {
            axios.get(baseURL).then((response) => {
                setPelis(response.data);
                console.log(response.data);
            });
        }, []);


        if (!pelis) return null;


        return (
            <div className="ui container" style={{ marginTop: '10px' }}>
                    <PelisList images={pelis}/>
            </div>
        );
}

export default Pelis;






