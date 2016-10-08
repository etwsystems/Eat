import {Component} from '@angular/core';
import {Http} from '@angular/http';
import 'rxjs/add/operator/map';
import {NavController} from 'ionic-angular';
import {MenuPage} from "../menu/menu";

@Component({
	templateUrl: 'build/pages/restaurant/restaurant.html',
	})

export class RestaurantPage {
    
    items:any;



	constructor(private http: Http, private navCtrl:NavController){

	this.http.get('http://127.0.0.1:8000/categories/?format=json&restaurant=1')
	.map(res => res.json())
		.subscribe(data => {
    		this.items = data;
		});

    
		
	}
	
click(event,item) {
        this.navCtrl.push(MenuPage,{
        	item:item,
        });
		console.log()
		}





}