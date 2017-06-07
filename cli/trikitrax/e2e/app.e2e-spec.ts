import { TrikitraxPage } from './app.po';

describe('trikitrax App', function() {
  let page: TrikitraxPage;

  beforeEach(() => {
    page = new TrikitraxPage();
  });

  it('should display message saying app works', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('app works!');
  });
});
