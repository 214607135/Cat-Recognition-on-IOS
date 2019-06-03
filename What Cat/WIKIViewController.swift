//
//  WIKIViewController.swift
//  What Cat
//
//  Created by JamesCullen on 2019/5/30.
//  Copyright © 2019年 JamesCullen. All rights reserved.
//

import UIKit
import Alamofire
import SwiftyJSON
import SDWebImage

class WIKIViewController: UIViewController {

    @IBOutlet weak var imageView: UIImageView!
    @IBOutlet weak var wikiDescription: UILabel!
    
    // The wikipedia URL.
    let wikipediaURl = "https://en.wikipedia.org/w/api.php"
    
    override func viewDidLoad() {
        super.viewDidLoad()
        requestWIKI(wikiRequest: wikiRequest)
        self.navigationItem.title = wikiRequest
    }

    func requestWIKI(wikiRequest: String){
        let parameters : [String:String] = [
            "format" : "json",
            "action" : "query",
            "prop" : "extracts|pageimages",
            "exintro" : "",
            "explaintext" : "",
            "titles" : wikiRequest,
            "indexpageids" : "",
            "redirects" : "1",
            // To ensure the quility of wiki images.
            "pithumbsize" : "500"
        ]
        
        Alamofire.request(wikipediaURl, method: .get, parameters: parameters).responseJSON { (response) in
            if response.result.isSuccess {
                if debug == true {
                print("Get infomation from WIKI successful!")
                print(response)
                }
                
                let catJSON : JSON = JSON(response.result.value!)
                
                let pageid = catJSON["query"]["pageids"][0].stringValue
                
                let catDescription = catJSON["query"]["pages"][pageid]["extract"].stringValue
                
                let catImageURL = catJSON["query"]["pages"][pageid]["thumbnail"]["source"].stringValue
                
                self.imageView.sd_setImage(with: URL(string: catImageURL ))
                self.wikiDescription.text = catDescription
                //                text = catDescription
                
                
            }
        }
    }
}
