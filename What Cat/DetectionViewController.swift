//
//  DetectionViewController.swift
//  What Cat
//
//  Created by JamesCullen on 2019/5/29.
//  Copyright © 2019年 JamesCullen. All rights reserved.
//

import UIKit
import Firebase
import Photos
import FirebaseFirestore


var chosenImage : UIImage?
var wikiRequest : String = ""
var debug : Bool = true

class DetectionViewController: UIViewController,  UIImagePickerControllerDelegate, UINavigationControllerDelegate {
    
    var storage: Storage!
    var firestore: Firestore!
   
    
    let imagePicker = UIImagePickerController()

    
    @IBOutlet weak var imageView: UIImageView!
    @IBOutlet weak var getMoreInfo: UIButton!
    @IBOutlet weak var processInfo: UILabel!
    @IBOutlet weak var confidence: UILabel!
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        imagePicker.delegate = self
        imagePicker.allowsEditing = false
        storage = Storage.storage()
        firestore = Firestore.firestore()
        // Do any additional setup after loading the view.
    }
    
    @IBAction func cameraPressed(_ sender: Any) {
        if debug == true {
            print("Camera button pressed!0000000000000000000000000")
        }
        let actionSheet = UIAlertController(title: nil, message: nil, preferredStyle: .actionSheet)
        
        actionSheet.addAction(UIAlertAction(title: "Camera", style: .default , handler:{ (UIAlertAction)in
            self.imagePicker.sourceType = .camera
            self.present(self.imagePicker, animated: true, completion: nil)
            if debug == true {
            print("User choose camera 0000000000000000000000000")
            }
        }))
        
        actionSheet.addAction(UIAlertAction(title: "Choose From Album", style: .default , handler:{ (UIAlertAction)in
            self.imagePicker.sourceType = .photoLibrary
            self.present(self.imagePicker, animated: true, completion: nil)
            if debug == true {
            print("User choose photo 0000000000000000000000000")
            }
        }))
        
        actionSheet.addAction(UIAlertAction(title: "Cancel", style: .cancel, handler:nil))
        
        present(actionSheet, animated: true)
    }
    
    @objc func image(_ image: UIImage, didFinishSavingWithError error: Error?, contextInfo: UnsafeRawPointer) {
        if let error = error {
            // we got back an error!
            let ac = UIAlertController(title: "Save error", message: error.localizedDescription, preferredStyle: .alert)
            ac.addAction(UIAlertAction(title: "OK", style: .default))
            present(ac, animated: true)
        } else {
            let ac = UIAlertController(title: "Saved!", message: "Reselect from photo library.", preferredStyle: .alert)
            self.processInfo.text = "Reselect from photo library."
            ac.addAction(UIAlertAction(title: "OK", style: .default))
            present(ac, animated: true)
        }
    }
    
    func imagePickerController(_ picker: UIImagePickerController, didFinishPickingMediaWithInfo info: [UIImagePickerController.InfoKey : Any]) {
        if let userImage = info[UIImagePickerController.InfoKey.originalImage] as? UIImage {
            chosenImage = userImage
            self.processInfo.text = ""
            self.confidence.text = ""
            if self.imagePicker.sourceType == .camera{
                UIImageWriteToSavedPhotosAlbum(userImage, self, #selector(image(_:didFinishSavingWithError:contextInfo:)), nil)
            }else{
                self.processInfo.text = "Waiting for uploading image..."
                self.imageView.image = chosenImage
                let imageURL = info[UIImagePickerController.InfoKey.imageURL] as? URL
                let imageName = imageURL?.lastPathComponent
                let storageRef = storage.reference().child("images").child(imageName!)
                
                storageRef.putFile(from: imageURL!, metadata: nil) { metadata, error in
                    if let error = error {
                        self.processInfo.text = "Try to upload photo again!"
                        print(error)
                    } else {
                        self.processInfo.text = "Upload Successfully!"
                        if debug == true {
                        print("Upload Successfully!0000000000000000000000000")
                        }
                        self.firestore.collection("predicted_images").document(imageName!)
                            .addSnapshotListener { documentSnapshot, error in
                                if let error = error {
                                    if debug == true {
                                    print("error occurred\(error) 0000000000000000000000000")
                                    }
                                } else {
                                    if (documentSnapshot?.exists)! {
                                        let imageData = (documentSnapshot?.data())
                                        self.visualizePrediction(imgData: imageData)
                                    } else {
                                        self.processInfo.text = "Waiting for processing..."
                                        if debug == true {
                                        print("processing!0000000000000000000000000")
                                        }
                                    }
                                }
                        }
                    }
                }
            }
        
        
            
        }

        
        imagePicker.dismiss(animated: true, completion: nil)
    }
    
    func visualizePrediction(imgData: [String: Any]?) {
        //        print("11111111111")
        //        print(imgData)
        let detect_confidence = imgData!["confidence"] as! Double * 100
        let label_id = imgData!["label_name"] as! Int
        let cat_name = self.catID(id: label_id)
        wikiRequest = cat_name
        
        if (imgData!["image_path"] as! String).isEmpty {
            self.processInfo.text = "Unable to find any cat."
        } else {
            let predictedImgRef = storage.reference(withPath: imgData!["image_path"] as! String)
            predictedImgRef.getData(maxSize: 1 * 1024 * 1024) { data, error in
                if let error = error {
                    if debug == true {
                    print(error)
                    }
                } else {
                    let image = UIImage(data: data!)
                    chosenImage = image
                    self.processInfo.text = cat_name
                    self.confidence.text = "\(String(format: "%.2f", detect_confidence))% confidence"
                    self.imageView.image = image
                }
            }
        }
        
    }
    

    func catID(id: Int) -> String{
        switch id {
        case 1:
            return "Abyssinian cat"
        case 2:
            return "American Bobtail cat"
        case 3:
            return "American Shorthair cat"
        case 4:
            return "Bengal cat"
        case 5:
            return "Birman cat"
        case 6:
            return "Bombay cat"
        case 7:
            return "British Shorthair cat"
        case 8:
            return "Egyptian Mau cat"
        case 9:
            return "Exotic cat"
        case 10:
            return "Maine Coon cat"
        case 11:
            return "Persian cat"
        case 12:
            return "Ragdoll cat"
        case 13:
            return "Russian Blue cat"
        case 14:
            return "Scottish Fold cat"
        case 15:
            return "Siamese cat"
        case 16:
            return "Siberian cat"
        case 17:
            return "Sphynx cat"
        default:
            return "No cat detected"
        }
    }

    }
