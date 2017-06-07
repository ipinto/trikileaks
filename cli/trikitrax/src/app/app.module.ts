import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';

import { AppComponent } from './app.component';
import { DragulaModule } from "ng2-dragula";
import { MomentModule } from "angular2-moment";

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    MomentModule,
    DragulaModule,
    BrowserModule,
    FormsModule,
    HttpModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
