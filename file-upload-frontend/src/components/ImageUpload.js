// Filename - App.js

import { useState } from "react";

export let isUploaded = false;


function ImageUpload() {
	const [file, setFile] = useState();
	function handleChange(e) {
		console.log(e.target.files);
		setFile(URL.createObjectURL(e.target.files[0]));
        isUploaded = true;
	}

	return (

		<div className="ImageUpload">
            {   

                isUploaded?  (
                    <div class="d-flex justify-content-center m-5">
                        <img src={file} />
                    </div>
                ) : (
                    <div>
                        <div class="m-2">
                            <strong> Please upload your file </strong>
                        </div>
			            <input type="file" class="form-control" onChange={handleChange} />
                    </div>
                )
            }    
			
		</div>
	);
}

export default ImageUpload;
