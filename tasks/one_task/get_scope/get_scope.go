package main

import (
 "fmt"
 "math"
 "math/rand"
 "time"
)

const TIMESTAMPS_COUNT = 50000

const PROBABILITY_SCORE_CHANGED = 0.0001

const PROBABILITY_HOME_SCORE = 0.45

const OFFSET_MAX_STEP = 3

type Score struct {
 Home int
 Away int
}

type ScoreStamp struct {
 Offset int
 Score  Score
}

func main() {
 var stamps = fillScores()

 for _, stamp := range *stamps {
  fmt.Printf("%v: %v -- %v\n", stamp.Offset, stamp.Score.Home, stamp.Score.Away)
 }

}

func generateStamp(previousValue ScoreStamp) ScoreStamp {
 random := rand.New(rand.NewSource(time.Now().UnixNano()))

 scoreChanged := random.Float32() > 1-PROBABILITY_SCORE_CHANGED
 homeScoreChange := 0
 if scoreChanged && random.Float32() > 1-PROBABILITY_HOME_SCORE {
  homeScoreChange = 1
 }

 awayScoreChange := 0
 if scoreChanged && homeScoreChange == 0 {
  awayScoreChange = 1
 }

 offsetChange := int(math.Floor(random.Float64()*OFFSET_MAX_STEP)) + 1

 return ScoreStamp{
  Offset: previousValue.Offset + offsetChange,
  Score: Score{
   Home: previousValue.Score.Home + homeScoreChange,
   Away: previousValue.Score.Away + awayScoreChange,
  },
 }
}

func fillScores() *[]ScoreStamp {

 scores := make([]ScoreStamp, TIMESTAMPS_COUNT)
 prevScore := ScoreStamp{
  Offset: 0,
  Score:  Score{Home: 0, Away: 0},
 }
 scores[0] = prevScore

 for i := 1; i < TIMESTAMPS_COUNT; i++ {
  scores[i] = generateStamp(prevScore)
  prevScore = scores[i]
 }

 return &scores
}

/*
 Takes list of game's stamps and time offset for which returns the scores for the home and away teams.
    Please pay attention to that for some offsets the game_stamps list may not contain scores.
*/
