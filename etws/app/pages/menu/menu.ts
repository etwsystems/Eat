import {Component} from '@angular/core';
import {Http} from '@angular/http';
import 'rxjs/add/operator/map';
import {NavController, NavParams} from 'ionic-angular';
import {OrderService} from '../../providers/order-service/order-service';

@Component({
	templateUrl: 'build/pages/menu/menu.html',
	})

export class MenuPage {
    
	test:any;
    item: any;
    posts: any;

	constructor(private http: Http, private navCtrl:NavController, private navParams:NavParams, public orderService: OrderService){

    this.item = navParams.get('item');

    this.orderService.getOrders().then((orders) => {
    this.test = JSON.parse(orders);
    
    })

	this.http.get('http://127.0.0.1:8000/menupage/?categoriesno='+ encodeURI(this.item.categoriesno)+'&format=json')
	.map(res => res.json())
	.subscribe(data => {
    this.posts = data;
	});


		
	}
	
click(event, post){
	this.orderService.addOrder(post.itemname);
	this.orderService.getOrders().then((orders)=>{this.test = JSON.parse(orders)});
}


remove(event, post){
    this.orderService.remove(post);
    console.log("test")
}


}