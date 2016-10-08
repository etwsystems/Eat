import {Component} from '@angular/core';
import {Http} from '@angular/http';
import 'rxjs/add/operator/map';
import {NavController} from 'ionic-angular';
import {RestaurantPage} from "../restaurant/restaurant";

@Component({
	templateUrl: 'build/pages/pick/pick.html',
	})

export class PickPage {
    
    posts:any;

	constructor(private http: Http, private navCtrl:NavController){

	this.http.get('http://127.0.0.1:8000/restaurant/?format=json')
	.map(res => res.json())
	.subscribe(data => {
    this.posts = data;
	});


		
	}
	
click() {
        this.navCtrl.push(RestaurantPage)
		console.log('console');
	}





}