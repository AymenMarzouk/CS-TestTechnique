import { TestBed } from '@angular/core/testing';

import { HistoriquetestService } from './historiquetest.service';

describe('HistoriquetestService', () => {
  let service: HistoriquetestService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(HistoriquetestService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
