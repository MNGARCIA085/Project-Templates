import React from "react";
import 'bootstrap/dist/css/bootstrap.min.css';


const ImageList = (props) => {

    return (
        <div>
          <h3><center>Lista de pelis</center></h3>
          <br></br>
          
          <table class="table table-bordered" data-pagination="true">
            <thead>
              <tr>
                <th>Título</th>
                <th>Descripción</th>
              </tr>
            </thead>
            <tbody>
              {props.images.map((item) => (
                <tr key={item.id}>
                  <td>{item.title}</td>
                  <td>{item.description}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      );


}

export default ImageList;



/**
 * const images = props.images.map ( ( image) => {
        return (
            <div>


                <table>
                    <th>sada</th>
                    <td>{image.title}</td>
                    <td>{image.description}</td>
                </table>


                
            </div>
        )
    })

    return <div className="image-list">{images}</div>
 */