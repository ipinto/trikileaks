export class Tweet {
  id: number;
  text: string;
  user: string;
  date_created: Date;

  constructor (tweet) {
    this.id = tweet.id;
    this.text = tweet.text;
    this.user = tweet.user;
    this.date_created = new Date(tweet.date_created);
  }

}
