import { Injectable } from '@angular/core';
import { Http } from '@angular/http';
import 'rxjs/add/operator/map';
import {Storage, SqlStorage} from 'ionic-angular';





// export class Order {
// 	orderdetailno: number;
// 	itemno: number;
// 	quantity: number;

// 	constructor(orderdetailno: number, itemno: number, quantity: number) {
// 		this.orderdetailno = orderdetailno;
// 		this.itemno = itemno;
// 		this.quantity = quantity;
// }

// }


@Injectable()
export class OrderService {
  
  private storage;
  private item;
  private data;

  constructor() {
  
   	this.storage = new Storage(SqlStorage, {name:'orders'});

   	
  }

public getOrders(){
	return this.storage.get('orders');
}


public addOrder(item){
	if(!this.data){
		this.data=[item]
	let sql = JSON.stringify(this.data);
	this.storage.set('orders', sql);
	}
	else{
    this.data.push(item);
	let sql = JSON.stringify(this.data);
	this.storage.set('orders', sql);
	}
}


remove(item) {
	for (var i=0; i<this.data.length; i++){
		if(item == this.data[i]){
			this.data.splice(i,1);
			break;
		}
	}
	let sql = JSON.stringify(this.data);
	this.storage.set('orders', sql);
	return this.getOrders();

}




}

