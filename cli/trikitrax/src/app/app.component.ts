import { Component } from '@angular/core';
import { Observable } from 'rxjs/Rx';
import { Http } from "@angular/http";
import { Tweet } from "./tweet";

@Component({
  selector: 'queued-songs',
  templateUrl: './app.component.html',
  styleUrls: ['./dragula.min.css']
})
export class AppComponent {
  private tweets = [];
  private endpoint = 'http://localhost:8080/songs';

  constructor (private http: Http) {
    this.http = http;
    Observable.interval(1000 * 3).subscribe(s => {
      this.getSongs();
    });
  }

  public remove(tweet_to_remove) {
    this.http.delete(this.endpoint + "/" + tweet_to_remove.id).subscribe(response => {
      if (response.ok) {
        this.tweets = this.tweets.filter(tweet => tweet !== tweet_to_remove);
      } else {
        // TODO: show error
      }
    });
  }

  private getSongs() {
    this.http.get(this.endpoint).subscribe(response =>
      response.json().map(tweet => {
        if (!this.tweets.some(t => t.id === tweet.id)) {
          return this.tweets.push(new Tweet(tweet))
        }
      })
    );
  };


}
