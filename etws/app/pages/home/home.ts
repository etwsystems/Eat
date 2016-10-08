import {Component} from '@angular/core';
import {Http, Headers, RequestOptions} from '@angular/http';
import 'rxjs/add/operator/map';
import {NavController, AlertController} from 'ionic-angular';
import {FormBuilder, Control, Validators} from '@angular/common';
import {RestaurantPage} from "../restaurant/restaurant";
import {PickPage} from "../pick/pick";
import {Device} from 'ionic-native';

@Component({
	templateUrl: 'build/pages/home/home.html',
	})

export class HomePage {
    
    data:any;
    usernameControl: any;
    error:any;
    reply:any;
    text:any;
    text2:any;

	constructor(private http: Http, private navCtrl:NavController, private alertCtrl: AlertController){
		this.data = [];
		this.data.username = "";
		this.data.password = "";
		this.data.password2 = "";
		this.data.email = "";
		this.data.ph = "";

	};


presentAlert() {
  let alert = this.alertCtrl.create({
    title: 'Incomplete information',
    subTitle: this.error,
    buttons: ['Try Again']
  });
  alert.present();
}	


click2(){
	let username = this.data.username;
	let password = this.data.password;
	var filter = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
	// var passfilter=
	if (!username){


		console.log("no username");
		this.error="Please enter username";
		this.presentAlert();
	}

	else if(!password) {
		this.error = "Please enter password";
		this.presentAlert();
		console.log("different password")

	}

	else if(password.length<5) {
		this.error = "Please enter password";
		this.presentAlert();
		console.log("different password")

	}
	else if(this.data.password != this.data.password2) {
		this.error = "Password does not match";
		this.presentAlert();
		console.log("different password")

	} else if(!filter.test(this.data.email)){

		this.error='Invalid email'
		this.presentAlert();
		console.log('invalid email');


	}else if(!this.data.ph) {
		this.error='Please enter valid phone number'
		this.presentAlert();
		console.log('no phone number')
	}
	else{
	// this.text=username;
 //   	this.text2=(Device.device.version);


	 //  var data = JSON.stringify({
  //       "orderno": 11030,
  //       "orderdate": "2016-01-01",
  //       "orderamount": "20.50",
  //       "customerno": 1,
  //       })
  //       let headers = new Headers({ 'Content-Type': 'application/json' });
  //       let options = new RequestOptions({ headers: headers });
  //  this.http.post('http://127.0.0.1:8000/restpost/', data, options).map(res => res.json())
  // .subscribe(data => {
  //   this.reply = data;
  // })
  // ;
  console.log(this.reply)
	this.navCtrl.push(PickPage);
	}
}



}