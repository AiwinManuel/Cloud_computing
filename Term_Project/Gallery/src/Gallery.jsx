import React, { useState, useEffect , useRef } from 'react';
import LightGallery from 'lightgallery/react';

// import styles
import 'lightgallery/css/lightgallery.css';
import 'lightgallery/css/lg-zoom.css';
import 'lightgallery/css/lg-thumbnail.css';
import 'lightgallery/css/lg-autoplay.css';
import 'lightgallery/css/lg-fullscreen.css';
import 'lightgallery/css/lg-share.css';
import 'lightgallery/css/lg-rotate.css';


// import plugins if you need
import lgThumbnail from 'lightgallery/plugins/thumbnail';
import lgZoom from 'lightgallery/plugins/zoom';
import lgAutoplay from 'lightgallery/plugins/autoplay'
import lgFullscreen from 'lightgallery/plugins/fullscreen';
import lgShare from 'lightgallery/plugins/share';
import lgRotate from 'lightgallery/plugins/rotate';

export function Gallery() {
    const [images, setImages] = useState([]);
    const fileInputRef = useRef(null);
    const [apiUrl, setApiUrl] = useState('');


    useEffect(() => {
        fetch('https://mztju5l4yc.execute-api.us-east-1.amazonaws.com/Prod/test')
          .then(response => response.json())
          .then(data => {
            const body = JSON.parse(data.body);
            setApiUrl(body.ApiGatewayEndpoint);
          })
          .catch(error => console.error('Error fetching API URL:', error));
      }, []);

    // Function to fetch images
    const fetchImages = async () => {
        try {
            const response = await fetch(`${apiUrl}/list`);
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            const data = await response.json();
            if (data.images) {
                const imageArray = data.images.map((src, index) => ({ src, alt: `Image number ${index + 1}` }));
                setImages(imageArray);
            } else {
                throw new Error('No images found');
            }
        } catch (error) {
            console.error('Failed to fetch images:', error);
        }
    };
    

    // Fetch images on mount
    useEffect(() => {
        if (apiUrl) { 
            fetchImages();
        }
    }, [apiUrl]);

    const handleUploadClick = () => {
        fileInputRef.current.click();
    };

    const handleFileChange = async (event) => {
        const file = event.target.files[0];
        if (file) {
            const base64 = await convertToBase64(file);
            uploadImage(base64, file.name);
        }
    };

    const convertToBase64 = (file) => {
        return new Promise((resolve, reject) => {
            const fileReader = new FileReader();
            fileReader.readAsDataURL(file);
            fileReader.onload = () => {
                resolve(fileReader.result);
            };
            fileReader.onerror = (error) => {
                reject(error);
            };
        });
    };

    const uploadImage = async (base64, fileName) => {
        const body = JSON.stringify({
            fileName: fileName,
            fileContent: base64.split(',')[1], 
        });
        try {
            await fetch(`${apiUrl}/upload`, {
                method: 'POST',
                headers: {
                    "Content-Type": "application/json",
                },
                body: body,
            });
            console.log('Image uploaded successfully');
            fetchImages(); // Fetch the updated list of images
        } catch (error) {
            console.error('Failed to upload image:', error);
        }
    };

    return (
        <div className="App">
            <div className="header-container">
                <button className="upload-button" onClick={handleUploadClick}>
                    Upload 
                </button>
                <h1 className="gallery-heading">Gallery</h1>
                <input
                    type="file"
                    ref={fileInputRef}
                    style={{ display: 'none' }}
                    onChange={handleFileChange}
                    accept="image/*"
                />
            </div>
            <LightGallery
                speed={500}
                plugins={[lgThumbnail, lgZoom, lgAutoplay, lgFullscreen, lgRotate, lgShare]}
            >
                {images.map((image, index) => (
                    <a href={image.src} key={index}>
                        <img alt={image.alt} src={image.src} />
                    </a>
                ))}
            </LightGallery>
        </div>
    );
}