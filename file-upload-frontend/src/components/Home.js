import ImageUpload from "./ImageUpload";
// import isUploaded from "./ImageUpload"
import handleCanvasClick from "./DrawRectangle";

let isUploaded = false;

// Lets you use style more compactly
let style = {
    "min-height": "650px"
}


export function Home(){
    return (
        <div class="d-md-flex">

            <div class="flex-coloumn flex-grow-1">
                {/* In react, element binding is done using this also known for comments*/}
                <div class="card m-2" style={style}>
                    <div class="card-header text-center">
                        {
                            (!isUploaded) ? (
                            <strong> Upload Certificate to page</strong>
                        ) : (
                            <strong> Image uploaded successfully </strong>
                        )
                        }
                    </div>

                    <div class="card-body">
                        <ImageUpload/>

                        {
                            (canvas) ? (
                            <handleCanvasClick/>
                            ) : (<p></p>)
                        }
                    </div>

                </div>
            </div>
        </div>
    );
}

